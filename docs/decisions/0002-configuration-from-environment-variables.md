---
status: accepted
date: 2026-11-10
---

# Read configuration from environment variables with pydantic-settings

## Context and Problem Statement

The application needs settings that differ between machines and, later,
between environments, such as the application name now and a database
address in future. Values like these should not be hard-coded, and anything
secret must never be committed to the repository.

## Considered Options

* Constants hard-coded in the source
* A configuration file read at startup
* Environment variables read with pydantic-settings

## Decision Outcome

Chosen option: "environment variables read with pydantic-settings", because
settings come from the environment of the running process, which keeps
secrets out of the repository and lets the same code run on a laptop or on a
server without changes. pydantic-settings turns them into a typed, validated
setting object, so a missing or mistyped value is caught when the application
starts.

Local values live in a `.env` file, which git ignores. A committed
`.env.example` lists every setting. Each setting has a default in the code, so
the file is optional, and settings without a sensible fallback (a database
address, later) will be required.

### Consequences

* Good, because secrets stay out of the repository, and the same code runs
  on a laptop or on a server with only the environment changing.
* Good, because settings are typed and validated in one place, so a bad value
  fails at startup with a clear message.
* Bad, because the settings live outside the code, so `.env.example` has to
  be kept in step with the settings class by hand.
* Bad, because it adds a dependency (pydantic-settings), though it shares its
  foundation with FastAPI.
