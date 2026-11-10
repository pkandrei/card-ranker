---
status: accepted
date: 2026-11-10
---

# Use uv for dependency and environment management

## Context and Problem Statement

The project needs a way to declare its dependencies, pin the exact versions
that were tested, create an isolated environment and fix the Python version,
so that a fresh clone can be set up the same way on any machine.

## Considered Options

* pip with a virtual environment and a `requirements.txt`
* uv

## Decision Outcome

Chosen option: "uv", because it covers all four jobs (declaring
dependencies, locking versions, creating the environment and selecting the
Python version) in one tool, and a fresh clone can be set up with a single
command.

Dependencies are declared in `pyproject.toml`, the exact resolved versions
are committed in `uv.lock`, and `.python-version` pins the Python version.

### Consequences

* Good, because setup is one command and the lock file makes installs
  reproducible.
* Bad, because contributors need uv installed, which is less universal than
  pip.