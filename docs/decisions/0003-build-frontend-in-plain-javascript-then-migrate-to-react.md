---
status: accepted
date: 2026-11-10
---

# Build the frontend in plain JavaScript first, then migrate to React

## Context and Problem Statement

The backend exposes an API, and a separate frontend calls it. The frontend
can be written in plain HTML, CSS and JavaScript or in a framework such as
React, and the choice also decides when React is learned.

## Decision Drivers

* Reaching a working application quickly, using tools already familiar
* Relevance of React to the current job market
* Learning value, including the experience of migrating a frontend
* Keeping a later migration small

## Considered Options

* Plain HTML, CSS and JavaScript only
* React from the start
* Plain first, then migrate to React page by page
* Plain first, then migrate to React in one step

## Decision Outcome

Chosen option: "plain first, then migrate to React in one step", because
familiar tools bring the project to a working state first, and the later
migration to React, which is more relevant to the job market, becomes both
a learning opportunity and practice at migrating a frontend, something not
done before.

The migration is planned as its own milestone (M5), finished when every
page runs on React, the plain frontend is removed and every existing
feature behaves as before. Until then, the plain frontend is structured to
keep the migration small: API calls live in one file, state is kept
separate from the code that draws the page, the interface is built from
small self-contained pieces, and CSS is organised per piece.

### Consequences

* Good, because a working application exists sooner, built with tools
  already known.
* Good, because the migration gives experience of moving a codebase to a
  new framework, as well as of React itself.
* Good, because the API does not change, so the backend is unaffected by
  the migration.
* Bad, because the frontend is written twice, and the plain version is
  eventually discarded.
* Bad, because keeping the migration small depends on following the
  structuring habits consistently.

## Pros and Cons of the Options

### Plain HTML, CSS and JavaScript only

* Good, because it needs no build tooling and no extra dependencies.
* Good, because it uses tools already familiar.
* Bad, because React is more relevant to the job market, and this option
  leaves it unlearned.
* Bad, because managing state and updating the page by hand becomes harder
  as the application grows.

### React from the start

* Good, because there is no rewrite and React is practised from the first
  day.
* Bad, because learning React and building the application at the same
  time slows reaching a working state.

### Plain first, then migrate to React page by page

* Good, because each step is small, and the application keeps working
  throughout.
* Bad, because the application temporarily contains two frontends that
  must work together.

### Plain first, then migrate to React in one step

* Good, because the application never mixes two frontends, and the
  plain version is removed completely.
* Bad, because the migration is one larger piece of work.