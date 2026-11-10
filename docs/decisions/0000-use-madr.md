---
status: accepted
date: 2026-11-10
---

# Use MADR for decision records

## Context and Problem Statement

Card Ranker involves choices that are easy to forget the reasons for, such
as the framework, the database and how data is modelled. Without a written
record, the reasoning is lost, and later changes risk repeating a discussion
that was already settled. The project needs a lightweight, consistent way
to record decisions as they are made.

## Considered Options

* No formal records (reasoning stays in commit messages, issues and pull
  requests)
* A free-form notes file
* Markdown Architectural Decision Records (MADR)

## Decision Outcome

Chosen option: "MADR", because it gives every record the same structure
while staying plain Markdown that lives next to the code and is versioned
with it.

Records are stored in `docs/decisions/` and named
`NNNN-title-with-dashes.md`, numbered from 0000 (this record). Both MADR
variants are used, chosen by the size of the decision: the minimal variant
for small decisions, and the full variant, which adds pros and cons for each
option, for decisions where the comparison is the substance.

### Consequences

* Good, because the reasoning behind each decision can be found later
  without digging through history.
* Bad, because every significant decision now costs a short write-up.