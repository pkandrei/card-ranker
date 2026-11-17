---
status: accepted
date: 2026-11-16
---

# Read the application version from pyproject.toml

## Context and Problem Statement

The API documentation shows the application's version, and a later issue
needs it again for the User-Agent sent to Scryfall. The version is
already declared in `pyproject.toml`, so a second copy in the code would
drift from it. The project needs one place that owns the version and one
way for the application to read it, including a defined behaviour when
the version cannot be found.

## Decision Drivers

* One source of truth for the version
* Working with the project as it is, a virtual uv project that is not
  installed as a package (see
  [0007](0007-add-project-root-to-pytest-import-path.md))
* A missing or damaged file should not stop the application from starting
* Behaviour that can be tested, including the failure cases

## Considered Options

* Read `pyproject.toml` at startup
* Read the installed package's metadata
* Define the version as a constant in the code

## Decision Outcome

Chosen option: "read `pyproject.toml` at startup", because it keeps the
version in the one file that already declares it and works without
installing the project as a package.

The code has two layers. `read_file_for_version` takes a path, reads the
version with the standard library's TOML reader and returns it. If the
file is missing, cannot be read, is not valid TOML or has no `version`
entry under `[project]`, it logs a warning that says which case it was
and returns the placeholder "unknown". `get_version` works out where
`pyproject.toml` is relative to the code, not to the working directory,
calls the first function and caches the result. `main.py` calls it once
when the application is created.

A version that cannot be found shows as "unknown" instead of stopping the
application, because a label in the documentation is not worth refusing
to start for.

### Consequences

* Good, because the version has one owner, and bumping it in
  `pyproject.toml` is the only step.
* Good, because nothing needs installing for the lookup to work.
* Good, because each failure case is tested and reports itself, and one
  test checks that the application's own lookup reaches the real file.
* Good, because the application still starts when the lookup fails.
* Bad, because the container image will have to include `pyproject.toml`.
  To be settled when the image is built.
* Bad, because the lookup depends on where the files sit. Moving either
  one makes the version show "unknown", though the test of the real file
  fails when that happens.
* Bad, because the warning is not yet visible when the server runs under
  uvicorn. Logging is set up in a later change.
* Bad, because making `app` an installable package later would replace
  this approach with package metadata, and would also revisit
  [0007](0007-add-project-root-to-pytest-import-path.md).

## Pros and Cons of the Options

### Read `pyproject.toml` at startup

* Good, because it keeps the version in the file that already declares
  it.
* Good, because it works with the project as it is.
* Bad, because it depends on the file's location relative to the code.
* Bad, because the deployed image must contain the file.

### Read the installed package's metadata

* Good, because it is the standard way for an installed package to learn
  its own version.
* Good, because it does not depend on file locations.
* Bad, because the project is virtual and `app` is not installable, so
  there is no installed package to ask.
* Bad, because making it installable needs a build system and is a
  larger change than this PR.

### Define the version as a constant in the code

* Good, because it is the simplest option and cannot fail.
* Bad, because the version would then be declared twice, and the two
  copies would drift apart.