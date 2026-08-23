# BDD Test Suite — Behave + Playwright

A behavior-driven test suite using Gherkin feature files (Behave) with
Playwright driving the browser. Tests run against
[saucedemo.com](https://www.saucedemo.com), a public site built for QA
practice.

## What's covered

- **Login** (`features/login.feature`): valid login, invalid password,
  locked-out user, and missing-credential scenarios (via Scenario Outline)
- **Inventory & cart** (`features/inventory.feature`): adding/removing
  products, cart badge count, sorting products by price

## Project structure

```
bdd-playwright-suite/
├── features/
│   ├── login.feature          # Gherkin scenarios for login
│   ├── inventory.feature      # Gherkin scenarios for cart/inventory
│   ├── environment.py         # Behave hooks: Playwright browser lifecycle
│   └── steps/
│       ├── login_steps.py     # Step definitions for login.feature
│       └── inventory_steps.py # Step definitions for inventory.feature
├── .github/workflows/
│   └── bdd-tests.yml          # CI: runs the suite on push/PR
├── behave.ini                 # Behave config
├── requirements.txt
├── .gitignore
└── README.md
```

## 1. Local setup

1. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   python -m pip install -r requirements.txt
   ```

2. Install the Playwright browser binary (one-time):
   ```
   playwright install --with-deps chromium
   ```

## 2. Running the tests

Run everything:
```
behave
```

Run a single feature file:
```
behave features/login.feature
```

Run with the browser visible instead of headless (useful for debugging):
```
set HEADLESS=false          # Windows
export HEADLESS=false       # macOS/Linux
behave
```

Failed scenarios automatically save a screenshot to `reports/screenshots/`.

## 3. Continuous Integration

`.github/workflows/bdd-tests.yml` runs the full suite headless on every
push/PR to `main`, and uploads failure screenshots as a build artifact
if anything fails. No setup needed beyond pushing to GitHub — the
workflow picks it up automatically.

## 4. Push to GitHub

1. Confirm nothing sensitive is staged:
   ```
   git status
   ```

2. Initialize and commit:
   ```
   git init
   git add .
   git commit -m "Project 5: BDD suite with Behave and Playwright"
   ```

3. Create a new repo on GitHub, then connect and push:
   ```
   git remote add origin https://github.com/<your-username>/bdd-playwright-suite.git
   git branch -M main
   git push -u origin main
   ```

4. Check the **Actions** tab on GitHub — the workflow should run
   automatically and show green once it passes.
