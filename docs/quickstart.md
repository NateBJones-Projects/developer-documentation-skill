# Quickstart

Use this guide to install `developer-documentation` and create a checked documentation set for one project.

## Requirements

- The complete `developer-documentation` directory.
- An AI host that supports Agent Skills.
- Access to the project that needs documentation.
- Python 3 if you want to use the bundled validator.

## Install the skill

Place the complete `developer-documentation` directory in your host's skill directory.

For a Codex project, the resulting path is:

```text
PROJECT/.agents/skills/developer-documentation/SKILL.md
```

For a Codex user installation, the resulting path is:

```text
~/.agents/skills/developer-documentation/SKILL.md
```

For a Claude Code project, the resulting path is:

```text
PROJECT/.claude/skills/developer-documentation/SKILL.md
```

Do not copy only `SKILL.md`. The skill loads its writing and documentation-type references when the job requires them. Restart the host if the skill does not appear after installation.

## Create documentation

Open a task in the project that contains the current code, tests, schemas, configuration, interface, and existing documentation.

Invoke the skill with the result you need:

```text
$developer-documentation Create a README and quickstart for this project. Test every command and keep the existing API reference intact.
```

For a narrow task, name the document and reader:

```text
$developer-documentation Write an installation guide for a developer setting up this CLI on a new Mac.
```

For a complete documentation set, name the required pages and entry point:

```text
$developer-documentation Build a documentation set with an overview, quickstart, concepts, CLI reference, and troubleshooting. Use docs/index.md as the entry page.
```

## Review the result

Confirm that the result does the following:

- identifies the intended reader and task;
- reflects the current implementation;
- labels unverified behavior or examples;
- keeps proposals separate from implemented features;
- uses one entry page for a multi-page set;
- links related pages with descriptive text;
- states prerequisites before procedures;
- gives the expected result when readers need to verify success.

## Run the Markdown checker

From the directory that contains `developer-documentation`, check one file or directory:

```bash
python3 developer-documentation/scripts/validate_docs.py \
  PATH_TO_DOCUMENTATION
```

Check GitHub-style heading links when the documentation uses them:

```bash
python3 developer-documentation/scripts/validate_docs.py \
  --check-fragments \
  PATH_TO_DOCUMENTATION
```

The command exits with status `0` when all checked files pass. It exits with status `1` and lists each issue when a check fails.

## Continue with the reference

Use the [skill reference](reference.md) for the supported document types, source order, writing rules, validator options, and package layout.
