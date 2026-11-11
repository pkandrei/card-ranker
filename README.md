# Card Ranker

A Magic: The Gathering deck-building companion that scores and ranks your cards, synergies included.

Deciding what to keep and what to cut is one of the hardest parts of deck building. Card Ranker lets the user break each card down into properties they rate themselves, such as mana cost, speed and impact. By letting the user mark synergies between cards, which raise or lower each other's scores, the ranking reflects how cards work together, not just on their own. Every card is then scored and ranked, so it becomes obvious which ones earn their place.

## Status

Card Ranker is in early development. The project is being set up, and so far only a minimal API with a health check and its first test exists. See [Getting started](#getting-started) to run it and its tests.

## Planned features

- Build decks and add cards, with each card matched to Scryfall data so its image and text appear automatically
- Rate cards with fixed mana values and custom tags, organised into groups
- Mark synergies between cards that raise or lower each other's scores
- See every card in a deck ranked on a leaderboard
- Log in with an account from any device
- Automatically link cards that had no match once they appear in the dataset

## Roadmap

Development is planned in milestones, tracked on GitHub: [view the milestones](https://github.com/pkandrei/card-ranker/milestones).

### Possible later additions

- Importing a card's tags automatically from Scryfall Tagger
- Format legality checks (Commander, Standard and so on)
- Deck imports from other sites, such as Archidekt or Moxfield
- A suggestion system for new cards
- Filtering out cards

## How scoring works

Each card's score is built from three layers:

1. **Mana:** a base value from the card's mana cost and colour burden, where cheaper and easier-to-cast cards score higher.
2. **Tags:** custom tags the user can rate for speed, resilience and impact. Tags can be organised into groups, and each additional group counts for less, so no card inflates its score by piling on tags.
3. **Synergies:** links between cards that raise or lower each other's scores. A soft cap keeps them from running away, so strong cards with no synergies still hold their own.

Cards are then ranked by their final score.

## Tech stack

- **Python 3.14** as the project language
- **uv** for dependency and environment management
- **pydantic-settings** for configuration read from environment variables, with a local `.env` file
- **FastAPI** for the backend API
- **Uvicorn** as the server that runs it
- **pytest** for testing, with **httpx2** as the HTTP client behind FastAPI's test client

Planned, and subject to change as the project is set up:

- **SQLite** for data storage at first, moving to **PostgreSQL** when accounts are added, with **SQLAlchemy** and **Alembic** for models and migrations
- Plain **HTML, CSS and JavaScript** for the frontend, followed by a planned migration to **React**
- **Ruff** for code quality

## Getting started

### Prerequisites

Install [uv](https://docs.astral.sh/uv/getting-started/installation/). It reads the Python version from the project and installs it if needed.

### Install

```
git clone https://github.com/pkandrei/card-ranker.git
cd card-ranker
uv sync
```

### Configuration

`.env.example` lists every setting. Copying it to `.env` is optional, since every setting has a default, and `.env` is ignored by git.

### Run

```
uv run uvicorn app.main:app
```

The API is then available at http://127.0.0.1:8000.

### Check that it works

- http://127.0.0.1:8000/health returns `{"status": "ok"}`.
- http://127.0.0.1:8000/docs shows the interactive API documentation, titled with the application name.

### Run the tests

`uv sync` already installs the testing tools, so the tests can be run straight away:

```
uv run pytest
```

All tests should pass.

## Licence and attribution

The code in this repository is released under the [MIT Licence](https://github.com/pkandrei/card-ranker/blob/main/LICENSE).

Card Ranker is unofficial Fan Content permitted under the Fan Content Policy. Not approved/endorsed by Wizards. Portions of the materials used are property of Wizards of the Coast. ©Wizards of the Coast LLC.

Card data and images come from [Scryfall](https://scryfall.com). Card Ranker is not affiliated with or endorsed by Scryfall, and card images are linked from Scryfall rather than stored or redistributed.
