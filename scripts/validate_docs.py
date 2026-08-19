#!/usr/bin/env python3
"""Validate the mechanical structure of local Markdown documentation."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
HTML_ID_RE = re.compile(r"\bid=[\"']([^\"']+)[\"']")


def markdown_files(inputs: list[Path]) -> tuple[list[Path], list[str]]:
    files: set[Path] = set()
    errors: list[str] = []

    for raw in inputs:
        path = raw.resolve()
        if not path.exists():
            errors.append(f"path does not exist: {raw}")
        elif path.is_file():
            if path.suffix.lower() != ".md":
                errors.append(f"not a Markdown file: {raw}")
            else:
                files.add(path)
        elif path.is_dir():
            files.update(
                candidate.resolve()
                for candidate in path.rglob("*.md")
                if not any(part.startswith(".") for part in candidate.relative_to(path).parts)
            )
        else:
            errors.append(f"unsupported path: {raw}")

    return sorted(files), errors


def strip_heading_markup(text: str) -> str:
    text = re.sub(r"\s+#+\s*$", "", text.strip())
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.replace("`", "")


def github_slug(text: str) -> str:
    text = strip_heading_markup(text).lower().strip()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def page_targets(path: Path) -> set[str]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
        return set()

    targets: set[str] = set()
    slug_counts: dict[str, int] = {}
    fence: tuple[str, int] | None = None

    for line in lines:
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1]:
                fence = None
            continue
        if fence is not None:
            continue

        for explicit in HTML_ID_RE.findall(line):
            targets.add(explicit)

        heading = HEADING_RE.match(line)
        if not heading:
            continue
        base = github_slug(heading.group(2))
        if not base:
            continue
        count = slug_counts.get(base, 0)
        slug_counts[base] = count + 1
        targets.add(base if count == 0 else f"{base}-{count}")

    return targets


def split_link_target(raw_target: str) -> tuple[str, str]:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]
    path_part, separator, fragment = target.partition("#")
    return unquote(path_part), unquote(fragment) if separator else ""


def is_external(target: str) -> bool:
    lowered = target.lower()
    return lowered.startswith(
        ("http://", "https://", "mailto:", "tel:", "data:", "javascript:")
    )


def validate_file(
    path: Path, check_fragments: bool, allow_empty_alt: bool = False
) -> list[str]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"{path}: not valid UTF-8: {exc}"]
    except OSError as exc:
        return [f"{path}: cannot read file: {exc}"]

    lines = text.splitlines()
    headings: list[tuple[int, int, str]] = []
    fence: tuple[str, int, int] | None = None
    content_lines: list[tuple[int, str]] = []

    for line_number, line in enumerate(lines, start=1):
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = (marker[0], len(marker), line_number)
            elif marker[0] == fence[0] and len(marker) >= fence[1]:
                fence = None
            continue
        if fence is not None:
            continue

        content_lines.append((line_number, line))
        heading = HEADING_RE.match(line)
        if heading:
            headings.append((line_number, len(heading.group(1)), heading.group(2)))

    if fence is not None:
        errors.append(f"{path}:{fence[2]}: unclosed fenced code block")

    if not headings:
        errors.append(f"{path}: missing level-one heading")
    else:
        if headings[0][1] != 1:
            errors.append(f"{path}:{headings[0][0]}: first heading must be level one")
        h1_count = sum(level == 1 for _, level, _ in headings)
        if h1_count != 1:
            errors.append(f"{path}: expected one level-one heading, found {h1_count}")

        previous_level = headings[0][1]
        for line_number, level, title in headings[1:]:
            if level > previous_level + 1:
                errors.append(
                    f"{path}:{line_number}: heading level skips from "
                    f"{previous_level} to {level}: {title}"
                )
            previous_level = level

    target_cache: dict[Path, set[str]] = {}
    for line_number, line in content_lines:
        for alt_text, _ in IMAGE_RE.findall(line):
            if not alt_text.strip() and not allow_empty_alt:
                errors.append(f"{path}:{line_number}: image needs alternative text")

        for link_text, raw_target in LINK_RE.findall(line):
            path_part, fragment = split_link_target(raw_target)
            if is_external(raw_target) or raw_target.startswith(("mailto:", "tel:")):
                continue

            if path_part:
                target_path = (path.parent / path_part).resolve()
                if not target_path.exists():
                    errors.append(
                        f"{path}:{line_number}: broken local link "
                        f"{link_text!r} -> {raw_target}"
                    )
                    continue
            else:
                target_path = path

            if check_fragments and fragment and target_path.is_file():
                targets = target_cache.setdefault(target_path, page_targets(target_path))
                if fragment not in targets:
                    errors.append(
                        f"{path}:{line_number}: missing heading target "
                        f"#{fragment} in {target_path}"
                    )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument(
        "--check-fragments",
        action="store_true",
        help="Check fragments against GitHub-style Markdown heading anchors.",
    )
    parser.add_argument(
        "--allow-empty-alt",
        action="store_true",
        help="Permit empty alternative text on images confirmed to be decorative.",
    )
    args = parser.parse_args()

    files, errors = markdown_files(args.paths)
    if not files and not errors:
        errors.append("no Markdown files found")

    for path in files:
        errors.extend(
            validate_file(
                path,
                args.check_fragments,
                allow_empty_alt=args.allow_empty_alt,
            )
        )

    if errors:
        print(f"Documentation validation failed ({len(errors)} issue(s)):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Documentation validation passed: {len(files)} Markdown file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
