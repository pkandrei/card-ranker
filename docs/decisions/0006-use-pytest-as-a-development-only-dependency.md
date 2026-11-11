---
status: accepted
date: 2026-11-10
---

# Use pytest, with the testing tools as development-only dependencies

## Context and Problem Statement

The project needs a way to run automated tests, starting with a placeholder
test that checks the health endpoint. The tools used to run tests are not
needed to run the application, and FastAPI's test client needs an HTTP
client library installed alongside it.

## Decision Drivers

* Agreement with FastAPI's documentation, which uses pytest for its
  testing examples
* Learning value: building on earlier experience with unittest
* Keeping the runtime dependency list limited to what the application uses
  (see [0005](0005-install-fastapi-bare-with-plain-uvicorn.md))

## Considered Options

* unittest from the standard library
* pytest, installed as a regular dependency
* pytest, installed as a development-only dependency

## Decision Outcome

Chosen option: "pytest, installed as a development-only dependency",
because FastAPI's documentation uses pytest, and moving to it from
unittest, which is already familiar, is a small step that adds a widely
used tool to the project's skills. The tools are only needed to run tests,
so keeping them out of the runtime dependency list matches the project's
lean approach.

The HTTP client for FastAPI's test client is httpx2. Starlette's test
client now prefers httpx2, and with only the older httpx installed it still
works but warns that httpx is deprecated. Both pytest and httpx2 are
declared in the `dev` dependency group in `pyproject.toml`. uv installs
that group by default, so a plain `uv sync` still sets up a complete
environment, while a runtime-only install leaves the tools out.

### Consequences

* Good, because the examples in FastAPI's documentation apply directly.
* Good, because the runtime dependency list contains only what the
  application uses.
* Good, because setting up a fresh clone is still one command.
* Good, because the test run produces no deprecation warning.
* Bad, because the test tooling depends on Starlette's choice of HTTP
  client library, which has already changed once.
* Bad, because dependency groups are one more concept to know about.

## Pros and Cons of the Options

### unittest from the standard library

* Good, because it is part of Python, so nothing needs to be installed.
* Good, because it is already familiar.
* Bad, because FastAPI's documentation uses pytest, so its examples would
  need translating.
* Bad, because it adds nothing new to learn.

### pytest, installed as a regular dependency

* Good, because FastAPI's documentation uses it, so its examples apply
  directly.
* Good, because it is a small step from unittest.
* Bad, because it is a third-party dependency.
* Bad, because it would be installed wherever the application is
  installed, though nothing there runs tests.

### pytest, installed as a development-only dependency

* Good, because it has the advantages of the option above.
* Good, because the runtime dependency list stays limited to what the
  application uses.
* Bad, because it adds a concept (dependency groups) to learn.