---
status: accepted
date: 2026-11-10
---

# Install FastAPI bare, with plain uvicorn as the server

## Context and Problem Statement

FastAPI was chosen as the backend framework (see
[0004](0004-use-fastapi-as-backend-framework.md)). It can be installed bare
or with its `standard` extras, and it needs a separate server to run. The
project needs to decide how much to install up front.

## Considered Options

* `fastapi[standard]`
* Bare `fastapi` with `uvicorn[standard]`
* Bare `fastapi` with plain `uvicorn`

## Decision Outcome

Chosen option: "bare `fastapi` with plain `uvicorn`", because the standard
install bundles a server, a command-line tool, a deployment tool for a
hosting service the project does not use, a template engine, form parsing
and several validators. The project keeps its dependencies lean and adds
each one in the pull request that first needs it, which also makes each
addition a deliberate step and a chance to practise.

The server is started by calling uvicorn directly.

### Consequences

* Good, because the dependency list contains only what the project uses.
* Bad, because the server must be added separately, and there is no
  `fastapi` command to run the application.