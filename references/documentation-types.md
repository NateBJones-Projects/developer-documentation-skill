# Documentation types

Choose a page by the reader's job, not by the material that happens to be available.

## Overview

Use an overview when the reader needs orientation before taking action.

Include:

- what the system does;
- who should use it;
- the main parts or capabilities;
- the shortest route to a useful next page;
- important limits or status information.

Do not turn the overview into an exhaustive reference.

## README

Use a repository README as the front door for a developer who has just found or opened the project.

Include the smallest useful set of the following information:

- what the project is;
- current support or maturity status when it affects use;
- requirements;
- installation or setup;
- the shortest working example;
- development and test commands;
- links to detailed documentation;
- license, security, or contribution information when applicable.

Keep long reference tables and troubleshooting procedures in linked pages when the repository has a documentation set.

## Quickstart

Use a quickstart to get a prepared reader to the first useful result quickly.

Include:

- narrow prerequisites;
- one recommended installation or setup path;
- one complete example;
- the expected result;
- the next page for deeper work.

Avoid background explanations that interrupt the path. Link to a concept page when the explanation is useful but not required for success.

## Tutorial

Use a tutorial for guided learning. The reader should complete a coherent project and understand the main ideas through the work.

Include:

- the learning goal and finished result;
- prerequisites;
- a sequence that builds on itself;
- checkpoints that show progress;
- short explanations at the moment they become useful;
- cleanup when the tutorial creates resources.

Do not use a tutorial as the only source for exact interface details.

## How-to guide

Use a how-to guide for one practical goal. Assume the reader knows the basic system.

Include:

- a task-based title;
- prerequisites specific to the task;
- the shortest supported procedure;
- expected results and failure points;
- related tasks only when they help the current goal.

Avoid teaching the entire product inside the procedure.

## Concept or explanation page

Use a concept page when the reader needs a mental model, design rationale, or explanation of behavior.

Include:

- the concept and why it matters;
- the relationship between important parts;
- examples or diagrams when they reduce explanation;
- constraints and tradeoffs;
- links to tasks and reference material.

Do not disguise a decision proposal as settled product behavior.

## Reference

Use reference documentation when the reader needs exact facts while working.

Organize it predictably around the interface. Include names, syntax, types, required values, defaults, constraints, outputs, errors, compatibility, and permission requirements.

Prefer generated reference when the implementation provides a reliable schema or documentation generator. Add hand-written context for meaning, common use, and non-obvious behavior.

## API or SDK documentation

For each supported operation, class, or method, include the stable contract:

- purpose;
- authentication or permissions;
- request or call syntax;
- parameters and types;
- response or return value;
- errors;
- side effects;
- one representative example;
- version or compatibility notes when needed.

Verify the contract against code, schemas, tests, or the live service. Do not infer supported behavior from an implementation detail.

## CLI documentation

Document commands in the same hierarchy as the command-line interface. Include syntax, required arguments, optional flags, defaults, environment requirements, exit behavior, and examples.

Use `--help` output or the command parser as the source. Keep task procedures separate from the exhaustive command reference when the reference becomes hard to follow.

## Installation and setup

Include supported environments, prerequisites, permissions, exact steps, verification, update behavior, and safe removal. State what the installer changes.

Test a clean installation when possible. A successful run on an already configured machine does not prove the clean-install path.

## Troubleshooting

Organize troubleshooting around what the reader can observe.

For each issue, include:

- symptom or exact error;
- likely cause only when supported;
- diagnostic check;
- resolution;
- verification;
- escalation information when the reader cannot resolve it safely.

Do not list speculative causes as facts. Put destructive recovery steps after safer checks and label their effect.

## Operations runbook

Use a runbook for a recurring operational task or incident response.

Include:

- purpose and scope;
- prerequisites and permissions;
- conditions that permit the operation;
- ordered procedure;
- health checks;
- stop conditions;
- rollback or recovery;
- escalation owner or destination;
- record or evidence the operator must leave.

Separate routine operation from emergency action when their authority or risk differs.

## Migration or upgrade guide

State the supported starting versions and destination version. Explain breaking changes, prerequisites, backup or rollback, ordered changes, data effects, verification, and cleanup.

Give the reader a way to determine whether the migration succeeded. Do not describe rollback as safe unless it has been verified for the stated version and data state.

## Architecture decision record

Use an architecture decision record to preserve one consequential technical decision.

Include:

- status and date;
- decision context;
- constraints;
- considered options;
- the chosen decision;
- consequences and known tradeoffs;
- replacement or supersession information.

Record the decision that was made. Keep open design exploration in a proposal until the owner decides.

## Release notes and changelog

Record user-visible change, not the implementation diary. Include the version or date, added or changed behavior, fixed behavior, deprecations, breaking changes, security implications when safe to disclose, and action required from the reader.

Use consistent categories across releases. Link to migration instructions when a reader must act.
