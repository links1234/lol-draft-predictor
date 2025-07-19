# LoL Draft‑Based Win Predictor

**Local Python tool to predict League of Legends match outcomes based on draft, team, patch, and player features.**

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
   - [Fetch Leagues](#fetch-leagues)
   - [Fetch Schedule](#fetch-schedule)
   - [Interactive Python](#interactive-python)
5. [Project Structure](#project-structure)
6. [Testing](#testing)
7. [Development Workflow](#development-workflow)
8. [Contributing](#contributing)
9. [License](#license)

---

## Prerequisites

- **Python 3.8+** installed on your system.
- **Git** for version control.
- (Recommended) **VS Code** or any IDE comfortable with Python.

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/lol-draft-predictor.git
   cd lol-draft-predictor
   ```

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv          # create the virtualenv
   source venv/bin/activate      # macOS/Linux
   # OR on Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. **Environment variables**

   - Copy the example env file and update:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and set:
     ```ini
     LOLESPORTS_API_KEY=your_real_api_key_here
     ```

2. **Verify** that `.env` is listed in `.gitignore` to keep your key private.

---

## Usage

Once setup is complete and your virtual environment is active, you can run the following commands:

### Fetch Leagues

```bash
python scripts/fetch_leagues.py
```

Prints the list of Leagues available via the LoL Esports API.

### Fetch Schedule

1. Edit or create a new script in `scripts/fetch_schedule.py`:
   ```python
   from lolpredictor.api_client import LoLEsportsAPIClient

   client = LoLEsportsAPIClient()
   data = client.get_schedule([123, 456])  # replace with real league IDs
   print(data)
   ```
2. Run:
   ```bash
   python scripts/fetch_schedule.py
   ```

### Interactive Python

You can also import and use the client in a Python REPL or Jupyter notebook:

```python
from lolpredictor.api_client import LoLEsportsAPIClient
client = LoLEsportsAPIClient()
leagues = client.get_leagues()
print(leagues)
```

---

## Project Structure

```
lol-draft-predictor/
├── .env.example          # Template for your API key
├── .gitignore            # Ignored files (venv, .env, egg-info, etc.)
├── README.md             # This file
├── requirements.txt      # Pinned dependencies
├── setup.py              # Installable package definition
├── lolpredictor/         # Main package
│   ├── __init__.py       # Python package marker
│   └── api_client.py     # LoL Esports API wrapper
├── scripts/              # Utility scripts
│   └── fetch_leagues.py  # Example: fetch and list leagues
├── tests/                # Unit tests
│   └── test_api_client.py
└── venv/                 # Virtual environment (ignored)
```

---

## Testing

Run all unit tests with:

```bash
pytest -q
```

Ensure tests pass before merging any changes.

---

## Development Workflow

1. **Always activate** your virtualenv.
2. **Install new dependencies** via `pip install <pkg>` and update `requirements.txt`:
   ```bash
   pip install <new-package>
   pip freeze > requirements.txt
   ```
3. **Make changes** in feature branches:
   ```bash
   git checkout -b feature/your-feature-name
   # code, add tests
   git add .
   git commit -m "Add <feature>"
   git push -u origin feature/your-feature-name
   ```
4. Open a **Pull Request** on GitHub, request reviews, and merge once approved.

---

## Contributing

1. Fork the repo and clone your fork.
2. Follow the development workflow above.
3. Keep PRs small and focused.
4. Write or update tests for any new behavior.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Happy drafting!*

