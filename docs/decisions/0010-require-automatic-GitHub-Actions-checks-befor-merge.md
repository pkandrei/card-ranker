---
status: accepted
date: 2026-11-17
---

# Run the checks automatically with GitHub Actions and require them to merge

## Context and Problem Statement

The project's checks (the Ruff lint check, the Ruff format check and the
tests) are run by hand. Nothing stops a pull request from reaching main
with a lint error, a formatting problem or a failing test, so keeping main
healthy depends on remembering to run them. The project needs the same
checks to run automatically, and needs a way to make them a condition for
merging. Several details also have to be settled, because a workflow runs
third-party code on a machine with access to the repository: when it runs,
how its tools are installed, and how far it is trusted.

## Decision Drivers

* Catching failures before they reach main, and noticing if a merged result
  fails
* Keeping the number of tools and dependencies low (see
  [0005](0005-install-fastapi-bare-with-plain-uvicorn.md))
* Reproducible runs, with the same tool versions in CI and on a laptop
* A small attack surface for code that runs in the repository's workflow

## Considered Options

* No automation (the checks stay manual)
* GitHub Actions, with a ruleset that requires the checks before merging
* GitHub Actions, with the checks advisory only

## Decision Outcome

Chosen option: "GitHub Actions, with a ruleset that requires the checks
before merging", because it is the only option that makes the checks a
condition for merging and not a habit, and GitHub Actions is built into the
platform that already hosts the repository.

The workflow lives in `.github/workflows/checks.yml` and has one job with
separate steps: install the locked dependencies, run the Ruff lint check,
run the Ruff format check, and run the tests. Separate steps mean a failed
run shows which check broke. The details are:

* **Triggers:** pull requests to main, and pushes to main. While a pull
  request is open, the workflow runs when it is opened and on every new push
  to its branch, which checks the combined result of the branch and main
  before the merge. After a merge, the run on main checks the squashed
  commit that actually lands there, which no pull request run tests. Pushes
  to other branches are not checked separately, since the pull request run
  already covers them.
* **uv:** installed with the setup action published by the uv authors, the
  usual way to do this job. The uv version is pinned once, in
  `pyproject.toml`, so the action and a local uv follow the same
  requirement. The Python version is read from the project, not repeated in
  the workflow.
* **Dependencies:** installed with `uv sync --locked`, so the run fails if
  `uv.lock` is out of date, instead of updating it on the runner and hiding
  the mismatch.
* **Third-party actions:** referenced by full commit ID, with a comment
  naming the version, because a version tag is a label its owner can move.
  Updating a pin is a deliberate, reviewable change.
* **Permissions:** read-only access to the repository contents, and the
  checkout step does not keep the workflow's token afterwards, since no
  later step uses git.
* **Runner:** `ubuntu-latest`, as the closest match to an environment the
  application would really run in. GitHub moves that name to newer releases
  over time, which is accepted.
* **Caching:** the setup action's default, which enables the uv cache on
  GitHub-hosted runners, is left as it is.

A ruleset on main requires a pull request and the checks to pass. The
repository admin is on its bypass list in the mode that applies to pull
requests only: a failing pull request still shows red and blocks the merge
button, and merging anyway is a deliberate extra click, while direct pushes
to main stay blocked. The ruleset is a repository setting, not a file, so
nothing in the repository shows that it exists; this record is where it is
written down.

### Consequences

* Good, because a lint error, a formatting problem or a failing test can no
  longer reach main unnoticed, and a merged result that fails is noticed too.
* Good, because runs are reproducible: dependencies come from the lock file,
  third-party actions cannot change under the project, and CI and local
  development share one uv version.
* Good, because the workflow has read-only access and keeps no credentials,
  which limits what a compromised step could do.
* Bad, because the ruleset is outside the repository, so it has to be
  recreated by hand if the repository is ever moved, and it can be changed
  without leaving a trace in the history.
* Bad, because pinned actions and the pinned uv version go stale unless
  someone updates them. Automating that is a separate, later issue.
* Bad, because `ubuntu-latest` can change under the project, so a run can
  break without any change to the repository.
* Bad, because the bypass is an escape hatch that can be used by mistake,
  though it takes a deliberate click.
* Bad, because anyone whose uv version differs from the pin cannot run uv in
  the project until they install the required version, and moving the pin
  forward is a deliberate change to `pyproject.toml`.

## Pros and Cons of the Options

### No automation

* Good, because there is nothing to set up or maintain, and no third-party
  code runs in the repository.
* Bad, because the checks only run when someone remembers to run them, so
  failures can reach main.

### GitHub Actions, with a ruleset that requires the checks before merging

* Good, because failures block the merge, and the checks run on both pull
  requests and main.
* Good, because it needs no tool beyond the platform already in use.
* Bad, because it adds a third-party action to trust and pin, and a
  repository setting that no file records.

### GitHub Actions, with the checks advisory only

* Good, because failures show as red marks without any risk of blocking a
  merge by mistake.
* Bad, because nothing stops a failing pull request from being merged, so
  the checks depend on discipline, which is the problem this record is
  meant to solve.