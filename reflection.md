# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- When I ran it for the first time, the ui looks good, but there is a number range of 1 to 100,- but when I typed in 1 , it says to go more lower number 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

> The hint were sometimes backward and when i tried to start a new game, it stucked in the screen and I should reload a page to start a new game. 
> When I typed in high number, it says to go more high higher but the range is upto 100.
> I didn't see any hint on the screen.  

Input Used | Expected Behavior | Actual Behavior | Console Error / Output
(100) | Go higher | Go lower | Error as the range is 100.



## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
> ChatGpt Mini 5 connected with Vs code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
> While I was getting consfused to run a git command, Ai recommended running pip install -r requirements.txt and streamlit run app.py from the project folder(not the workspace root) and to add the project folder to PYTHONPATH when running tests. I verified it through the project directory, activated the virtualenv, ran pip install -r reuquirements.txt, started the app with streamlit run app.py and ran tests with PYTHONPATH=$(pwd) pytest -q. These steps resolved the original "file not found" and import errors.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
> Ai refactored check_guess to defensively convert inputs to int and return "Too Low" when conversion failed (treating non-numeric input as a low guess) which was misleading. Then, I reviewed logic_utils.py and saw the conversion logic and the fallback return "Too Low". I considered semantics and test coverage: tests in test_gamelogic.py/test_game_logic.py cover numeric outcomes but not non-numeric fallbacks, so returning "Too Low" for parse errors is semantically misleading. I reverted to a clearer behavior path (kept the refactor location but ensured comments and tests validate intended behavior). Verification included reading the code, inspecting tests, and re-running pytest to confirm explicit numeric outcomes still pass.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
>  I ran the app locally and exercised the full game flow (Easy/Normal/Hard), tried boundary and out‑of‑range guesses, and used the New Game flow to confirm state resets — when hints, attempt counts, and final outcomes matched expectations across those cases, I considered the bug fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
> I ran pytest (including the new test_gamelogic.py) which asserts get_range_for_difficulty, parse_guess, check_guess, and update_score behaviors; the tests verified the core logic returns expected outcomes (Win / Too High / Too Low) and score math is correct. I also did manual checks in the UI (entering high/low/invalid inputs) to verify the app displayed the corresponding hints and attempt counts.
- Did AI help you design or understand any tests? How?
> Yes, the AI suggested unit tests and the PYTHONPATH=$(pwd) approach to fix import errors; I used those suggestions to write and run tests, then verified results by re-running pytest and checking the UI.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
> Streamlit reruns the entire script on every user interaction (widget change, button press), so you should not rely on plain module-level variables to persist data across interactions. Use st.session_state to store game state (secret number, attempts, score, status, history) so values survive reruns. Calling st.rerun() forces an immediate rerun when you need to restart the app programmatically, and st.stop() can short-circuit rendering when appropriate. In short: the script is re-executed frequently, and st.session_state is the safe place for persistent UI state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  > The way I used git and the testing habit . 
- What is one thing you would do differently next time you work with AI on a coding task?
> Navigate and understand more code by myself. Alsom I’ll ask for suggested tests and expected edge cases before applying code changes, and I’ll require the AI to justify fallback behavior (so we avoid misleading defaults like treating parse errors as “Too Low”).
- In one or two sentences, describe how this project changed the way you think about AI generated code.
> AI is a fast, helpful pair-programmer that accelerates routine tasks and suggests fixes, but its suggestions must be validated with tests and human judgment — I now treat AI output as a draft that needs verification

