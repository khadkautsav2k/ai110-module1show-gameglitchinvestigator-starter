# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Game purpose:** A simple number-guessing game built with Streamlit where the player guesses a secret integer in a difficulty-dependent range. The UI shows hints (higher/lower), tracks attempts, and scores the player based on how quickly they win.
- **Bugs found:** Hints were sometimes reversed (telling the player to go higher when their guess was already higher than the secret). The game state could be reset unexpectedly across interactions and the core guess-checking logic was split between files, making it hard to test.
- **Fixes applied:** Centralized game logic into `logic_utils.py`, fixed the `check_guess` comparison so hints match the secret, added and ran unit tests for `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score`, and annotated the code with short collaboration comments documenting agent–user pairing.


## Demo Walkthrough

1. Start the app on `Normal` difficulty (range 1–100). Open "Developer Debug Info" and note the secret is 55.
2. User enters a guess of `40` and clicks Submit.
   - Game returns: "Too Low"
   - Score updates: 0 -> -5 (wrong guess penalty)
3. User enters a guess of `70` and clicks Submit.
   - Game returns: "Too High"
   - Score updates: -5 -> -10
4. User enters a guess of `55` and clicks Submit.
   - Game returns: "🎉 Correct!" and shows final score
   - Score updates: -10 -> 70 (win points: 100 - 10*(attempt_number-1) = 80 added)
5. Game state changes to `won`; further submits are disabled until New Game is pressed.

This textual walkthrough shows the end-to-end behavior (hints, scoring, attempts, and final state) without needing a screenshot.

## Test Output (Challenge 1: Advanced Edge-Case Testing)

The pytest run after the fixes produced:

```
.........                                                                [100%]
9 passed in 0.00s
```


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
