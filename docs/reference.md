# Skill reference

This page defines the inputs, behavior, output expectations, and validator interface for `developer-documentation` version `1.0.0`.

## Invocation

Use `$developer-documentation` in Codex. Hosts that use slash commands can expose it as `/developer-documentation`. A host can also select the skill automatically from the description in `SKILL.md`.

## Required inputs

The skill needs:

- the documentation request;
- the project or product being documented;
- access to current code, tests, schemas, configuration, command help, interfaces, runtime behavior, or authoritative product files;
- the required location and format when the user specifies them.

When the reader or output form is not explicit, the skill uses the project and request to make the narrowest reasonable choice. It asks for clarification only when different choices would materially change the result.

## Source order

The skill uses sources in this order:

1. The user's current request and corrections.
2. Project-specific instructions and terminology.
3. Current code, tests, schemas, configuration, command help, interfaces, and runtime behavior.
4. Existing project documentation.
5. Current official documentation for dependencies, platforms, or standards that can change.

The skill does not document a proposal as implemented behavior. It labels material claims that cannot be verified.

## Supported document types

| Type | Primary reader job |
|---|---|
| Overview | Understand what the system is and where to start. |
| README | Enter a repository and reach setup, use, development, and detailed documentation. |
| Quickstart | Reach the first useful result through the shortest supported path. |
| Tutorial | Learn the system through a complete guided sequence. |
| How-to guide | Complete one practical goal. |
| Concept page | Understand how or why the system works. |
| Reference | Find exact interface, field, command, default, constraint, output, and error details. |
| API or SDK documentation | Use a supported operation, class, method, request, or response. |
| CLI documentation | Use commands, arguments, flags, environment requirements, and exit behavior. |
| Installation guide | Set up, verify, update, or remove the system. |
| Troubleshooting | Diagnose an observable symptom and verify the resolution. |
| Operations runbook | Perform a recurring operation with checks, stop conditions, rollback, and escalation. |
| Migration guide | Move between supported states or versions and verify the result. |
| Architecture decision record | Preserve one technical decision, its context, and consequences. |
| Release notes | Understand user-visible changes and required action. |

For the detailed content contract for each type, see [documentation types](../references/documentation-types.md).

## Working method

The skill performs the following work:

1. Establishes the reader, task, scope, destination, and format.
2. Inspects the current system and existing documentation.
3. Selects the smallest documentation form that serves the reader.
4. Creates one entry page and one primary job per page for a multi-page set.
5. Writes direct procedures, exact reference material, and runnable examples.
6. Updates navigation and removes stale duplication when pages move.
7. Runs project documentation checks and tests examples when the environment permits it.
8. Reports any behavior or example that remains unverified.

## Writing standard

Project-specific language and style take priority. Otherwise, the skill uses:

- sentence-case headings;
- task headings that start with a base-form verb;
- noun-phrase headings for concepts and reference sections;
- active voice and second person;
- numbered steps when order matters;
- one main action per procedural step;
- code formatting for filenames, commands, flags, fields, and literal input;
- descriptive link text;
- meaningful image alternative text;
- direct American English without promotional language.

For the complete standard, see the [writing standard](../references/writing-standard.md).

## Validator command

Run the validator with one or more Markdown files or directories:

```bash
python3 scripts/validate_docs.py \
  [--check-fragments] \
  [--allow-empty-alt] \
  PATH [PATH ...]
```

Run the command from the `developer-documentation` directory, or use the absolute path to `scripts/validate_docs.py` from another directory.

## Validator arguments

| Argument | Required | Behavior |
|---|---|---|
| `PATH` | Yes | Checks a Markdown file or every non-hidden `.md` file under a directory. Accepts more than one path. |
| `--check-fragments` | No | Checks fragments against GitHub-style Markdown heading targets. |
| `--allow-empty-alt` | No | Permits empty image alternative text after the user confirms that each affected image is decorative. |

## Validator checks

The validator checks:

- each input path exists;
- file inputs use the `.md` extension;
- files decode as UTF-8;
- each file has one level-one heading;
- the first heading is level one;
- heading levels do not skip;
- fenced code blocks close;
- local link targets exist;
- optional GitHub-style heading fragments exist;
- images have alternative text unless decorative images are explicitly allowed.

The validator does not check external URLs, technical accuracy, sentence case, clarity, terminology, runtime behavior, or whether a command succeeds.

## Validator exit status

| Status | Meaning |
|---|---|
| `0` | Every checked file passed. |
| `1` | At least one input or documentation check failed. |
| `2` | Python argument parsing rejected the command. |

## Package layout

| Path | Purpose |
|---|---|
| `README.md` | Human entry point, installation summary, and package contents. |
| `SKILL.md` | Agent Skills metadata and working method. |
| `docs/quickstart.md` | First installation and documentation run. |
| `docs/reference.md` | Complete supported behavior and validator interface. |
| `docs/troubleshooting.md` | Common installation, source, and validation failures. |
| `references/documentation-types.md` | Detailed content contracts for supported document types. |
| `references/writing-standard.md` | Default editorial and formatting rules. |
| `scripts/validate_docs.py` | Dependency-free Markdown validator. |
| `tests/test_validate_docs.py` | Unit tests for the validator. |

## Boundaries

The skill does not:

- invent unsupported flags, fields, endpoints, defaults, or compatibility claims;
- report a proposal as an implemented feature;
- report an untested procedure as working;
- replace an existing project documentation build or checker when that system is available;
- publish documentation or change an external service without the user's authorization;
- store project documentation or continuing project state inside the skill folder.
