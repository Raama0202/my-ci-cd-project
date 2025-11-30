# my-ci-cd-project

![Tests](https://github.com/Raama0202/my-ci-cd-project/workflows/Automated%20Testing/badge.svg) ![CodeQL](https://github.com/Raama0202/my-ci-cd-project/workflows/CodeQL%20Security%20Analysis/badge.svg) ![Codecov](https://codecov.io/gh/Raama0202/my-ci-cd-project/branch/main/graph/badge.svg)

A compact CI/CD template demonstrating automated testing, linting, coverage and security scanning using GitHub Actions.

A complete Python project with automated testing and CI/CD integration using GitHub Actions.

## Project Structure

```
my-ci-cd-project/
├── app.py                 # Main application code
├── test_app.py           # Unit tests
├── requirements.txt      # Project dependencies
├── pytest.ini            # Pytest configuration
├── README.md             # This file
└── .github/
    └── workflows/
        ├── test.yml                  # Main CI/CD workflow for testing
        └── codeql-analysis.yml      # Security scanning workflow
```

## Features

✅ **Automated Testing** - Unit tests with pytest  
✅ **Multi-Platform Testing** - Tests run on Ubuntu, Windows, and macOS  
✅ **Multi-Version Testing** - Tests run on Python 3.9, 3.10, 3.11, 3.12  
✅ **Code Coverage** - Coverage reports with codecov integration  
✅ **Code Quality Checks** - Flake8, Black, isort linting  
✅ **Security Scanning** - CodeQL analysis  
✅ **Scheduled Runs** - Daily and weekly automated testing  

## Setup

### Local Development

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd my-ci-cd-project
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Web Application

1. **Run the Flask app:**
   ```bash
   python app.py
   ```

2. **Open your browser** and go to `http://127.0.0.1:5000`. You should see the To-Do list application running.

### Running Tests Locally

```bash
# Run all tests with coverage
pytest --cov=app --cov-report=html

# Run tests in parallel
pytest -n auto

# Run with verbose output
pytest -v

# Run specific test file
pytest test_app.py
```

### Code Quality Checks

```bash
# Lint with Flake8
flake8 app.py test_app.py

# Format with Black
black app.py test_app.py

# Sort imports with isort
isort app.py test_app.py
```

## GitHub Actions Workflows

### 1. Automated Testing (`test.yml`)

**Triggers:** Push to main/develop, PR to main/develop, daily at midnight UTC

**Features:**
- Runs on Ubuntu, Windows, macOS
- Tests on Python 3.9, 3.10, 3.11, 3.12
- Code quality checks (Flake8, Black, isort)
- Coverage reporting with Codecov
- Parallel test execution with pytest-xdist
- Detailed test reports

### 2. Security Scanning (`codeql-analysis.yml`)

**Triggers:** Push to main/develop, PR to main/develop, weekly on Monday

**Features:**
- CodeQL analysis for security vulnerabilities
- Automatic code analysis

## Badge

Add this to your README to show the CI/CD status:

```markdown
![Tests](https://github.com/<your-username>/<your-repo>/workflows/Automated%20Testing/badge.svg)
```

## Contributing

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for guidelines.

## License

MIT License - See LICENSE file for details
