---
status: accepted
date: 2026-11-10
---

# Use FastAPI as the backend framework

## Context and Problem Statement

The backend is written in Python and exposes an API that a separate
frontend calls (see
[0003](0003-build-frontend-in-plain-javascript-then-migrate-to-react.md)).
A web framework is needed to build that API.

## Decision Drivers

* Relevance of the framework to the current job market, since the project
  also serves as a learning exercise
* Fit with an API-only backend that has a separate frontend
* Fit with the planned data layer (SQLAlchemy and Alembic) and with
  pydantic-settings, already in use

## Considered Options

* FastAPI
* Django
* Flask

## Decision Outcome

Chosen option: "FastAPI", because it is built for exactly this shape of
project, an API behind a separate frontend, and it fits the data layer
already chosen. Job relevance was the deciding factor between the options
that fit.

### Consequences

* Good, because request and response validation, and interactive API
  documentation, come from type hints with no extra code.
* Good, because it works with SQLAlchemy and Alembic, and shares its
  Pydantic foundation with pydantic-settings.
* Bad, because it provides no ORM, authentication or admin interface, so
  these are chosen and assembled separately.
* Bad, because it is younger than the other two and has fewer conventions
  for structuring a project.

## Pros and Cons of the Options

### FastAPI

* Good, because it is designed for building APIs.
* Good, because validation and generated documentation come from type hints.
* Good, because it leaves the choice of database layer open.
* Bad, because authentication and similar parts must be added separately.
* Bad, because its ecosystem is smaller and younger than Django's or Flask's.

### Django

* Good, because it is mature and includes an ORM, migrations,
  authentication and an admin interface.
* Good, because it has a very large ecosystem and is widely used.
* Bad, because its ORM and migrations would replace the chosen SQLAlchemy
  and Alembic, or sit awkwardly beside them.
* Bad, because it is built around server-rendered pages, and an API-only
  backend uses a small part of it, typically with an extra package such as
  Django REST framework.

### Flask

* Good, because it is small, simple and flexible, with a large ecosystem.
* Good, because it works with SQLAlchemy and Alembic.
* Bad, because validation and API documentation need extensions, which
  FastAPI includes by design.
* Bad, because type-hint-driven development is not central to its design.