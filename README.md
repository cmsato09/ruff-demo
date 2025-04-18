# Quick Intro to Ruff
Notes on [Ruff](https://docs.astral.sh/ruff/) and initializing a project using the uv package manager.

Presentation given to Hacker Dojo Python Meetup on 2025/04/08.

## Install uv

- Install uv depending on your local machine by following the docs. (https://docs.astral.sh/uv/getting-started/installation/)
- `uv self update` 
    - If you already have uv installed, update it. 
- `uv --version`
    - Checks the current version
- If you cloned a repo that uses uv, run `uv sync`
    - "the dev group is special-cased and synced by default," so you won't need additional flags specifically for any dev dependencies.
- References
    - https://docs.astral.sh/uv/getting-started/installation/
    - https://docs.astral.sh/uv/reference/cli/#uv-self-update

## Initialize a Python Project with uv

- `uv init`
    - Creates a python project in current working directory. Good to use when you created and changed to a directory.
- `uv init <PATH>`
    - Create a directory at PATH within current working directory. 
- `uv init --python 3.13`
    - Creates project in working directory and a virtual environment with python 3.13
    - "Some project state is not created until needed, e.g., the project virtual environment (.venv) and lockfile (uv.lock) are lazily created during the first sync."
- During `uv init`, the following are generated.
    - .git folder
    - .gitignore file
    - .python-version file
    - main.py file
    - pyproject.toml file
    - README.md file
- `uv venv`
    - Create a virtual environment (.venv folder) with the latest python interpreter downloaded(?)
- References
    - https://docs.astral.sh/uv/getting-started/installation/
    - https://docs.astral.sh/uv/reference/cli/#uv-init
    - https://docs.astral.sh/uv/reference/cli/#uv-venv

## Add Ruff as a Dependency

- `uv add --dev ruff`
    - Install as a dev dependency specific to the project.
- `uv tool install ruff`
    - Install as global standalone tool available to all projects.
- `uv add` will also create a uv.lock file if not present. 
- To explicity create a uv.lock file, use the command `uv lock`
- References
    - https://docs.astral.sh/ruff/tutorial/
    - https://docs.astral.sh/uv/reference/cli/#uv-add
    - https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies
    - https://docs.astral.sh/uv/concepts/tools/

## Use Ruff as a Linter

- `uv run ruff check`
    - By default, checks all Python files in the current directory and subdirectory 
- `uv run ruff check <file_directory>`
    - Checks all Python files in specific file directory
- `uv run ruff check <specific_file_path>`
    - Checks specific file
- `uv run ruff check --fix`
    - This command automatically fixes the linting issue at hand.
    - Doesn’t fix everything. There are some lines you have to fix yourself
- References
    - https://docs.astral.sh/ruff/linter/
- Notes
    - *If you’re not using uv, disregard `uv run`
    - *If you’re using ruff as a uv tool, replace `uv run` with `uvx`, which is equivalent to `uv tool run`

## Use Ruff as a Formatter

- “Designed as a drop-in replacement for Black” → Adheres to Black’s code style
- `uv run ruff format`
    - By default, formats all Python files in the current directory and subdirectory 
- `uv run ruff format <file_directory>`
    - Formats all Python files in specific file directory
- `uv run ruff format <specific_file_path>`
    - Formats specific python file
- References
    - https://docs.astral.sh/ruff/formatter/
    - [Black Playground](https://black.vercel.app/?version=stable&state=_Td6WFoAAATm1rRGAgAhARYAAAB0L-Wj4ASJAnldAD2IimZxl1N_WlkPinBFoXIfdFTaTVkGVeHShArYj9yPlDvwBA7LhGo8BvRQqDilPtgsfdKl-ha7EFp0Ma6lY_06IceKiVsJ3BpoICJM9wU1VJLD7l3qd5xTmo78LqThf9uibGWcWCD16LBOn0JK8rhhx_Gf2ClySDJtvm7zQJ1Z-Ipmv9D7I_zhjztfi2UTVsJp7917XToHBm2EoNZqyE8homtGskFIiif5EZthHQvvOj8S2gJx8_t_UpWp1ScpIsD_Xq83LX-B956I_EBIeNoGwZZPFC5zAIoMeiaC1jU-sdOHVucLJM_x-jkzMvK8Utdfvp9MMvKyTfb_BZoe0-FAc2ZVlXEpwYgJVAGdCXv3lQT4bpTXyBwDrDVrUeJDivSSwOvT8tlnuMrXoD1Sk2NZB5SHyNmZsfyAEqLALbUnhkX8hbt5U2yNQRDf1LQhuUIOii6k6H9wnDNRnBiQHUfzKfW1CLiThnuVFjlCxQhJ60u67n3EK38XxHkQdOocJXpBNO51E4-f9z2hj0EDTu_ScuqOiC9cI8qJ4grSZIOnnQLv9WPvmCzx5zib3JacesIxMVvZNQiljq_gL7udm1yeXQjENOrBWbfBEkv1P4izWeAysoJgZUhtZFwKFdoCGt2TXe3xQ-wVZFS5KoMPhGFDZGPKzpK15caQOnWobOHLKaL8eFA-qI44qZrMQ7sSLn04bYeenNR2Vxz7hvK0lJhkgKrpVfUnZrtF-e-ubeeUCThWus4jZbKlFBe2Kroz90Elij_UZBMFCcFo0CfIx5mGloKoK10y5eFtrgIZy3gUg3-VibDzoc8fXF63NR9AgKYXS1NQPXDXEwAAAABk7Jx28oPV2QABlQWKCQAAjbEry7HEZ_sCAAAAAARZWg==)
- Notes
    - Again, *if you’re not using uv, disregard `uv run`
    - *If you’re using ruff as a uv tool, replace `uv run` with `uvx`, which is equivalent to `uv tool run`

## Default Configurations

- Configuration rules are stored in pyproject.toml or ruff.toml
- List of Rules (https://docs.astral.sh/ruff/rules/)
- Let’s add to our configurations
    - In the pyproject.toml file, add the following lines to the `[tool.ruff.lint]` section. Basically added “I” to the default settings to get iSort to work. 
        - `select = ["E4", "E7", "E9", "F", “I”]`
    - Another thing we can try is to ignore a warning. Add the following lines to the `[tool.ruff.lint]` section. Adding “F401” to ignore will suppress the unused import warning. 
        - `ignore = [“F401”]`
- References
    - https://docs.astral.sh/ruff/configuration/

## Integration with pre-commit

- You can use Ruff as a GitHub Action, but using it as a pre-commit may be a better way to enforce style consistency during the commit stage instead of when you are pushing to a repo. 
- Use pre-commit in your project (https://pre-commit.com/#install)
    1. Install pre-commit as a dev dependency with `uv add --dev pre-commit`
    2. Create a `.pre-commit-config.yaml` file
    3. Copy paste the ruff pre-commit hook from https://github.com/astral-sh/ruff-pre-commit
    4. Run `uv run pre-commit install` to set up the git hook script
    5. Optional step: Run pre-commit hook against all files when adding new hooks with `uv run pre-commit run --all-files`
- References
    - https://docs.astral.sh/ruff/integrations/

## Resources
- Real Python Podcast: Ep 238 – Charlie Marsh: Accelerating Python Tooling With Ruff and uv (https://www.youtube.com/watch?v=hGFb4mMMmkE)
- PyCon US 2024 Talk - Charlie Marsh: Ruff: An Extremely Fast Python Linter and Code Formatter, Written in Rust (https://www.youtube.com/watch?v=r1EZ3GXuwBA)
- Pybites Podcast #175 - Charlie Marsh on Ruff, uv and designing fast + ergonomic Python tooling (https://www.youtube.com/watch?v=byynvdS_7ac)
