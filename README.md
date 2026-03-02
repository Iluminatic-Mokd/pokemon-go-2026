# pokemon-go-2026

This repository contains a Flask web application that manages users and Pokémon entries.

## Getting started

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # PowerShell
# or for cmd.exe use
# .\.venv\Scripts\activate.bat
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Initialize the database

A helper script creates a SQLite database in the project root:

```powershell
python scripts\create_db.py
```

You can also set the environment variables first to point to a different database:

```powershell
$env:DATABASE_URL='sqlite:///data.db'
$env:SECRET_KEY='dev'
python scripts\create_db.py
```

### 4. Run the development server

Flask requires a few environment variables so that it can locate the application and configure SQLAlchemy.

For **PowerShell**:

```powershell
$env:DATABASE_URL='sqlite:///data.db'
$env:SECRET_KEY='dev'
$env:FLASK_APP='main'
flask run --debug
```

For **cmd.exe**:

```cmd
set DATABASE_URL=sqlite:///data.db
set SECRET_KEY=dev
set FLASK_APP=main
flask run --debug
```

You can omit `--debug` if you prefer; it enables the interactive debugger and auto-reload.

> ⚠️ The `flask` command will complain with "Either 'SQLALCHEMY_DATABASE_URI' or 'SQLALCHEMY_BINDS' must be set" if the `DATABASE_URL` variable is missing. Make sure to export/set it before running the server.

When the server starts you can visit **http://127.0.0.1:5000/** in your browser.

---

The rest of this README can describe project structure, features, etc.
