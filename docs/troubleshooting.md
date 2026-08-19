# Troubleshooting

Use this page to resolve common installation, source, and validation problems for `developer-documentation`.

## The skill does not appear

Confirm that the complete folder exists at the path used by your host. The path must end with:

```text
developer-documentation/SKILL.md
```

Check that the folder name and the `name` field in `SKILL.md` are both `developer-documentation`. Restart the host after installing a new skill.

Do not install a second copy under another skill root with the same name. Remove or rename a conflicting copy only after you identify which version is current.

## The skill cannot verify a product claim

Give the task access to the current code, schema, command help, interface, test, runtime, or official external documentation that owns the claim.

If the source is unavailable, keep the limitation in the finished documentation. Do not convert an assumption or old document into a current fact.

## A documented command cannot be tested

Confirm that the current environment has the required runtime, dependencies, credentials, and safe test target. Do not use production or customer data merely to make a documentation claim.

If a safe test is not available, label the command as unverified or illustrative and state what prevented the test.

## The validator reports a broken local link

Read the reported source file, line number, link text, and target. Confirm that the destination exists relative to the source file.

Update the link when the page moved. Restore the page when the destination was removed by mistake. Do not add an empty placeholder only to make the check pass.

## Fragment checking fails on a valid heading

`--check-fragments` uses GitHub-style Markdown heading targets. A different publishing system can generate different targets.

Run the validator without `--check-fragments` when the project does not use GitHub-style anchors. Use the project's own link checker for the published target format.

## A decorative image fails the alternative-text check

Confirm that the image is truly decorative and communicates no information. Then run:

```bash
python3 scripts/validate_docs.py \
  --allow-empty-alt \
  PATH_TO_DOCUMENTATION
```

Do not use `--allow-empty-alt` to suppress missing descriptions for diagrams, screenshots, charts, or other informative images.

## Validator tests fail

From the directory that contains `developer-documentation`, run:

```bash
python3 -m unittest discover \
  -s developer-documentation/tests \
  -p "test_*.py"
```

Use Python 3. The tests require no third-party packages. If a test still fails, keep the exact failure output and compare the current validator with `docs/reference.md` before changing either one.
