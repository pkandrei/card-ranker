# card-ranker

A Magic: The Gathering deck-building companion that scores and ranks your cards, synergies included.

Deciding what to keep and what to cut is one of the hardest parts of deck building. Card Ranker lets the user break each card down into properties they rate themselves, such as mana cost, speed and impact. By letting the user mark synergies between cards, which raise or lower each other's scores, the ranking reflects how cards work together, not just on their own. Every card is then scored and ranked, so it becomes obvious which ones earn their place.

## Status

Card Ranker is in early development. The project is currently being planned and set up, and there is nothing to run yet.

## Planned features

- Build decks and add cards, with each card matched to Scryfall data so its image and text appear automatically
- Rate cards with fixed mana values and your own custom tags, organised into groups
- Mark synergies between cards that raise or lower each other's scores
- See every card in a deck ranked on a leaderboard
- Log in with an account from any device

### Possible later additions

- Importing a card's tags automatically from Scryfall Tagger
- Format legality checks (Commander, Standard and so on)
- Automatically linking cards that had no match once they appear in the dataset
- Allow deck imports from other deckbuilding sites, such as Archidekt or Moxfield
- A suggestion system for new cards

## How scoring works

Each card's score is built from three layers:

1. **Mana:** a base value from the card's mana cost and colour burden, where cheaper and easier-to-cast cards score higher.
2. **Tags:** custom tags you rate for speed, resilience and impact. Tags can be organised into groups, and each additional group counts for less, so no card inflates its score by piling on tags.
3. **Synergies:** links between cards that raise or lower each other's scores. A soft cap keeps them from running away, so strong cards with no synergies still hold their own.

Cards are then ranked by their final score.
