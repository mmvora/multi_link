# This is the MultiLink Codebase

Built on Django, using TailwindCSS and Webpack. 

by Malhaar Vora

## Prerequisites:

### Python Environment
I recommend using a virtual environment to install the requirements. (see [here](https://docs.python.org/3/library/venv.html) for more information on how to set up a virtual environment).
You will need python 3.12 or higher to run this project.

### Install poetry

Before installing `poetry`, you'll most likely want to install `pipx`.

```bash
brew install pipx
pipx ensurepath
```

Then install `poetry` using `pipx`.

```bash
pipx install poetry
```

With `poetry` installed you can use it to install the dependencies in your chosen virtual environment.

```bash
poetry install
```

### Setup ENVs

You will also need to setup the `.env` file. You can copy the `.env.example` file to `.env` and fill in the required values. 

```bash
cp .env.example .env
```

## Setup Database
You will also need to setup a local database of your choice. I personally use `postgresql` (for which you can just create a local version using the name `multilink`). See [here](https://docs.djangoproject.com/en/5.1/ref/databases/#postgresql-connection-settings) for the right way to setup in production,

## Start commands:
Frontend: `npm run start`

Backend: `poetry run python manage.py runserver`

## Formatting:
Run: `npm run fmt` for both djlint and ruff 