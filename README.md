# Developer documentation skill

`developer-documentation` is a standalone Agent Skills package for creating, restructuring, and maintaining accurate documentation for software, tools, automations, packages, APIs, SDKs, CLIs, installations, migrations, operations, and troubleshooting.

The skill reads the working system before it writes. It separates implemented behavior from proposals, chooses the documentation form that matches the reader's job, and checks the finished Markdown with a bundled validator.

## Download the skill

Download [developer-documentation-skill-1.0.0.zip](https://github.com/NateBJones-Projects/developer-documentation-skill/releases/download/v1.0.0/developer-documentation-skill-1.0.0.zip) from the first release. The ZIP contains one complete `developer-documentation` directory that you can place in your AI host's skill directory.

To follow the project or contribute changes, clone the repository:

```bash
git clone https://github.com/NateBJones-Projects/developer-documentation-skill.git developer-documentation
```

## Supported documentation

Use the skill for:

- READMEs and overview pages;
- quickstarts and tutorials;
- how-to and concept guides;
- API, SDK, CLI, and package references;
- installation and migration guides;
- operations runbooks;
- release notes;
- troubleshooting pages;
- complete linked documentation sets.

## Package contents

```text
developer-documentation/
├── README.md
├── SKILL.md
├── docs/
│   ├── quickstart.md
│   ├── reference.md
│   └── troubleshooting.md
├── references/
│   ├── documentation-types.md
│   └── writing-standard.md
├── scripts/
│   └── validate_docs.py
└── tests/
    └── test_validate_docs.py
```

`SKILL.md` contains the working method loaded by the AI host. The `docs` directory explains how to install, invoke, and operate the skill. The `references` directory contains detailed writing guidance. The validator and its tests are independent Python files with no third-party dependencies.

## Install the skill

Keep the complete `developer-documentation` directory together. Place it in the skill directory used by your AI host.

Common locations are:

| Host and scope | Destination |
|---|---|
| Codex project | `.agents/skills/developer-documentation` |
| Codex user | `~/.agents/skills/developer-documentation` |
| Claude Code project | `.claude/skills/developer-documentation` |
| Claude Code user | `~/.claude/skills/developer-documentation` |

Do not overwrite an existing directory with the same name until you confirm that it is obsolete. Restart the AI host if the newly installed skill does not appear.

## Use the skill

Invoke the skill by name and state the documentation result you need. For example:

```text
$developer-documentation Create a quickstart and CLI reference for this project. Verify every documented command.
```

The host can also select the skill automatically when the request clearly asks for developer documentation.

For a complete first run, see the [quickstart](docs/quickstart.md).

## Validate Markdown

Use the bundled validator when the project does not already have a documentation checker:

```bash
python3 developer-documentation/scripts/validate_docs.py PATH [PATH ...]
```

The validator checks UTF-8 decoding, heading structure, fenced code blocks, local links, and image alternative text. Add `--check-fragments` for GitHub-style heading targets. Add `--allow-empty-alt` only when every image with empty alternative text is confirmed to be decorative.

The validator does not prove that technical claims are correct or that commands work. The skill checks those against the current code, interface, tests, or runtime.

## Requirements

- Access to the code, interface, current behavior, or authoritative product files needed to verify the documentation.
- Python 3 only when you use the validator or run its tests.
- No third-party Python packages.

## Test the package

From the directory that contains `developer-documentation`, run:

```bash
python3 -m unittest discover \
  -s developer-documentation/tests \
  -p "test_*.py"
```

For the full interface and validation behavior, see the [skill reference](docs/reference.md). For common failures, see [troubleshooting](docs/troubleshooting.md).
