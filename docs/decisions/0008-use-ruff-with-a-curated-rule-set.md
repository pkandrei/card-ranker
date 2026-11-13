---
status: accepted
date: 2026-11-12
---

# Use Ruff for linting and formatting, with a curated rule set

## Context and Problem Statement

The project needs automated checks that catch likely mistakes and keep the
code style consistent, so that quality does not depend on remembering
conventions or on review alone. Ruff can do both jobs in one tool: linting
(reporting likely errors and bad practice) and formatting (applying one
fixed code style). Using one tool for both also fits the project's approach
of keeping tools and dependencies few (see
[0005](0005-install-fastapi-bare-with-plain-uvicorn.md)). What remains open
is which of Ruff's rule families to enable, since its defaults are small and
a broad set adds noise and upkeep, and where to keep the configuration.
The decision is made now because the codebase is still tiny: choosing the
rules costs almost nothing today, while adding them later would mean one
large clean-up once there is a lot of code.

## Decision Drivers

* Keeping the number of tools and dependencies low
* Every enabled rule family can be justified by a reason specific to this
  project
* Low noise, so findings are worth acting on and exceptions stay rare
* Catching problems early, while the cost of fixing them is small
* Code that follows common professional standards

## Considered Options

* Ruff's default rules only
* Ruff's defaults plus a curated set of rule families
* A broad rule set, with unwanted rules switched off one by one

## Decision Outcome

Chosen option: "Ruff's defaults plus a curated set of rule families",
because it checks meaningfully more than the defaults while every enabled
family still has a reason that can be stated in a sentence, and it avoids
the exceptions and upkeep of a broad set.

Ruff is used for both linting and formatting. The enabled families are:

* **I**, import sorting: keeps import blocks in one consistent order.
* **UP**, modernisation: flags older patterns where newer syntax exists,
  relevant on a recent Python version.
* **B**, likely bugs: catches well-known traps such as mutable default
  arguments.
* **PTH**, pathlib: keeps file handling consistent, which matters for the
  downloaded card data and the data folder.
* **DTZ**, timezone-aware dates: avoids naive datetimes, relevant to the
  deck creation date and to accounts later.
* **PT**, pytest style: checks how tests are written.
* **N**, naming: enforces the standard Python naming conventions.
* **FAST**, FastAPI: checks for common mistakes in route definitions.
* **C4**, comprehensions: tidies how lists, dicts and sets are built.
* **SIM**, simplifications: suggests shorter equivalent forms and nudges
  towards idiomatic Python.

Families considered and left out:

* **D** (docstrings) and **ANN** (type annotations everywhere): they add
  ceremony for little value on small, self-explanatory code.
* **PL** (Pylint-derived): large, opinionated and overlapping with other
  families.
* **S** (security): useful once accounts exist, but it would need
  exceptions now. To be revisited at the login milestone.
* **T20** (no print statements): it conflicts with the load summary and
  warnings, which are meant to appear in the terminal.
* **RUF** (Ruff's own rules): a mixed set with no single idea behind it,
  with some rules that can flag patterns that frameworks use deliberately.
  Deferred until SQLAlchemy models exist and show whether it helps.

The line length stays at Ruff's default of 88, and the formatter keeps its
defaults. The configuration lives in `pyproject.toml`, next to the other
project tooling, and the target Python version is taken from
`requires-python` rather than repeated.

Ruff is installed as a development-only dependency, like pytest, since it is
run on the code and not by the application.

### Consequences

* Good, because one tool and one configuration cover linting and
  formatting, keeping the dependency list short.
* Good, because every enabled family has a stated reason, and the left-out
  ones are recorded rather than forgotten.
* Good, because the rules are in place while the codebase is small, so no
  large clean-up is needed later.
* Bad, because a rule will occasionally flag code that is fine, and that
  needs a one-line exception.
* Bad, because the chosen set is a judgement, and it will need revisiting
  as the project grows (RUF and S are already marked for that).
* Bad, because rules are enabled by family, so a Ruff upgrade can bring new
  rules inside a family. The pinned version in `uv.lock` makes upgrades a
  deliberate step.

## Pros and Cons of the Options

### Ruff's default rules only

* Good, because it is quiet and needs almost no justification or upkeep.
* Good, because it never produces findings that are worth arguing with.
* Bad, because it checks little beyond basic errors, and later additions
  would mean a larger clean-up.

### Ruff's defaults plus a curated set of rule families

* Good, because each family has a reason specific to this project.
* Good, because it catches more than the defaults without much noise.
* Bad, because choosing the families is a judgement call that can be wrong
  and needs revisiting.

### A broad rule set, with unwanted rules switched off one by one

* Good, because it enforces the most, and signals strict standards.
* Bad, because some families are noisy or contradict each other, which
  leads to a growing list of exceptions to document and maintain.
* Bad, because it is a lot of upkeep for a project of this size.