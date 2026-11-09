# Instructions for Claude Code in this project

## My role and yours
- I (Plamenna) decide the design. The plan and the matching rules are in NOTES.md.
- You implement only the step I ask for, then stop and wait.
- If a rule in NOTES.md is unclear or seems wrong, ask me. Do not invent new rules or change mine silently.
- When I ask "is there a case where this fails?", answer with concrete examples from the data.

## Data safety
- Never modify, overwrite or rename anything in `data/`. Read from `data/`, write results only to `output/`.
- Never send the data to any external service.

## Code structure
- All logic in functions inside the `matcher/` package. No code at module level except `main()` under `if __name__ == "__main__":`.
- Small pure functions (normalise name, parse date, check AHV, compare two documents) that can be tested alone.
- Type hints on every function. Short docstring explaining *why*, not *what*.
- Prefer the standard library. Allowed extra packages: pandas, rapidfuzz, unidecode, pytest. Ask before adding anything else.

## Tests
- Every function with logic gets a test in `tests/`.
- When I name a dangerous case (for example "twins must not merge"), write that test first, then the code.
- Run the tests with `uv run pytest` after each step and show me the result.

## Environment (already set up by me before the session)
- Python 3.14, managed with uv. The environment is `.venv/`, created from `pyproject.toml` with `uv sync`.
- Run everything with `uv run ...` (for example `uv run pytest`). Do not activate other environments.
- Never use `pip install`. If a package is needed, ask me first, then use `uv add <package>` (or `uv add --dev <package>` for dev tools).
- Never create, delete or recreate `.venv/` yourself.

## How to run
- `uv run python -m matcher.main` writes `output/patients.json`.
- `uv run pytest` runs all tests.

## Style of your answers
- Short. Show the diff and one or two sentences on what changed.
- No large rewrites of files I didn't ask you to touch.
