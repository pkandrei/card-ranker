---
status: accepted
date: 2026-11-11
---

# Add the project root to pytest's import path

## Context and Problem Statement

The first test imports the application from the `app` package. `app` is a
plain folder in the project root, not an installed package, so Python only
finds it when the project root is on its import path. The test passed in
PyCharm, which adds the project root to the import path by default, but
failed from a terminal with a module-not-found error, because pytest puts
the folder of the test file (`tests/`) on the import path instead.

## Considered Options

* Set pytest's `pythonpath` option in `pyproject.toml`
* Always run `python -m pytest`
* Add an empty `conftest.py` in the project root
* Make `app` an installable package

## Decision Outcome

Chosen option: "set pytest's `pythonpath` option in `pyproject.toml`",
because it works with the plain `uv run pytest` command in a terminal, in
PyCharm and later in automated checks, and it states the project's
expectation in a file under version control.

Running `python -m pytest` needs no configuration, but plain `pytest` would
still fail, so the fix would live in a habit. An empty `conftest.py` works
through a side effect of how pytest finds configuration files, which is not
obvious to a reader. Making `app` an installable package is the most
thorough fix, but it needs a build system and is a larger change than this
PR.

The setting is `pythonpath = ["."]` in the `[tool.pytest.ini_options]`
section.

### Consequences

* Good, because the terminal and PyCharm now agree, with no extra command
  form or extra file.
* Bad, because the setting is specific to pytest, and becomes redundant if
  the project later becomes an installable package.