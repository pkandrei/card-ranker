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
setti