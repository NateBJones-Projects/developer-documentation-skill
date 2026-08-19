---
name: developer-documentation
description: Create, restructure, or maintain accurate developer documentation for software, tools, automations, packages, APIs, SDKs, CLIs, installations, migrations, operations, and troubleshooting. Use when the user asks for a README, overview, quickstart, tutorial, how-to guide, concept page, reference, API or CLI documentation, installation guide, runbook, migration guide, release notes, troubleshooting page, or a complete documentation set.
metadata:
  version: "1.0.0"
---

# Developer documentation

Create documentation that helps the intended reader understand or use the real system without needing its author beside them.

## Establish the documentation contract

Before writing:

1. Read the user's request and the instructions in the target project.
2. Inspect the current code, tests, schemas, configuration, command help, interfaces, and existing documentation that define the behavior.
3. Identify the reader, the job they need to complete, the documentation location, and the required output format.
4. Separate current behavior from proposed behavior. Do not document a proposal as an implemented feature.
5. Preserve unrelated documentation and user changes.

Use current product behavior as the source for product claims. Use official primary documentation for a dependency, platform, or standard that can change. If a material claim cannot be verified, label the limitation instead of filling the gap.

## Choose the right document type

Create only the pages the reader needs. Do not turn every request into a full documentation site.

Use these common forms:

- An overview explains what the system is, who it is for, and where to start.
- A quickstart gets a prepared reader to the first useful result through the shortest supported path.
- A tutorial teaches by guiding the reader through a complete learning sequence.
- A how-to guide helps an informed reader complete one goal.
- A concept page explains how or why the system works.
- A reference page states the exact interface, fields, commands, defaults, constraints, and errors.
- A troubleshooting page starts with observable symptoms and gives verified ways to diagnose and resolve them.
- An operations runbook gives an operator the prerequisites, safe procedure, checks, rollback, and escalation path for a recurring operation.
- A migration guide explains the starting state, destination state, compatibility limits, ordered changes, verification, and rollback.
- Release notes record user-visible changes, dates or versions, compatibility effects, and required action.

Read [documentation types](references/documentation-types.md) when the request needs several pages, the correct form is unclear, or the information architecture needs to change.

## Build the documentation set

For a multi-page set:

1. Choose one entry page.
2. Give each page one primary reader job.
3. Put the shortest useful path near the entry point.
4. Separate learning, task, explanation, and exact reference content when combining them makes the page hard to scan.
5. Link related pages with descriptive text.
6. Update or remove stale navigation when pages move.

Do not copy the same procedure across several pages. Keep one maintained procedure and link to it from the other pages.

## Write procedures

State prerequisites and permission requirements before the steps. Use numbered steps when order matters and bullets when it does not.

For each step:

1. Start with the action.
2. State the tool, screen, directory, or environment before the action when that context matters.
3. Put one main action in each step.
4. Explain placeholders immediately after the command or example that uses them.
5. State the expected result when it helps the reader continue or verify success.
6. Mark an optional step with `Optional:` at the start.

Prefer one supported path. Add alternatives only when different readers genuinely need them.

## Write reference documentation

Organize reference content around the public interface, not the source file layout. Derive exact names, types, required fields, defaults, return values, errors, and compatibility notes from the implementation or an authoritative schema.

For API, SDK, and CLI reference material:

- distinguish required, optional, and mutually exclusive inputs;
- show valid values and defaults;
- explain side effects and permission requirements;
- include representative success and failure output when it improves use;
- link to the maintained source of exhaustive generated reference when one exists;
- do not expose internal details that are not part of the supported contract.

## Create usable examples

Make examples minimal, runnable, and safe to copy. Use placeholders for secrets and user-specific values. Introduce each code block with the purpose of the code. Add a language identifier to fenced code blocks when the language is known.

Run commands and examples in a safe environment when possible. If an example cannot be run, say that it is illustrative. Never state that an installation, deployment, migration, or recovery procedure works unless the relevant boundary was tested.

## Apply the writing standard

Project-specific terminology and style take priority. Otherwise, follow [the developer documentation writing standard](references/writing-standard.md).

Use sentence-case headings, direct procedures, active voice, second person, American English, and one consistent term for each thing. Use code font for filenames, commands, flags, fields, methods, and text the reader must enter. Remove promotional claims, filler, fake certainty, and unexplained jargon.

## Verify the result

Run the project's documentation build, linter, link checker, or test suite when one exists. Test documented commands and examples in proportion to the risk. For a rendered documentation site, inspect the rendered pages and navigation.

For Markdown without an existing checker, run the bundled validator:

```bash
python3 "/path/to/developer-documentation/scripts/validate_docs.py" PATH [PATH ...]
```

The validator checks UTF-8 decoding, heading structure, fenced code blocks, local links, and image alternative text. Add `--check-fragments` when the documentation uses GitHub-style heading anchors.

Add `--allow-empty-alt` only when each image with empty alternative text is confirmed to be decorative.

The validator cannot prove technical accuracy, clarity, sentence case, or whether an example works. Check those against the real system.

## Finish the work

Deliver the finished documentation at the requested path. Report what changed, how the documentation was checked, and any specific behavior that remains unverified. Do not report a draft as published or an untested procedure as working.
