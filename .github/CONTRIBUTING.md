# Contributing to my-ci-cd-project

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Development Workflow

### 1. Fork and Clone

```bash
git clone https://github.com/<your-username>/my-ci-cd-project.git
cd my-ci-cd-project
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 3. Set Up Development Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Make Changes and Test

Write code that follows these standards:

- **Code Style:** Use Black for formatting
  ```bash
  black app.py test_app.py
  ```

- **Import Sorting:** Use isort
  ```bash
  isort app.py test_app.py
  ```

- **Linting:** Pass Flake8 checks
  ```bash
  flake8 app.py test_app.py
  ```

- **Testing:** Write tests and ensure all pass
  ```bash
  pytest --cov=app --cov-report=term-missing
  ```

### 5. Commit and Push

```bash
git add .
git commit -m "feat: add new feature"
git push origin feature/your-feature-name
```

### 6. Create a Pull Request

- Go to GitHub and create a PR from your branch to `main` or `develop`
- Fill in the PR template with details about your changes
- Ensure all CI/CD checks pass

## Requirements for Contributions

- ✅ All tests must pass
- ✅ Code coverage should not decrease
- ✅ Code must pass all linting checks
- ✅ Code must be formatted with Black
- ✅ Imports must be sorted with isort

## Testing Guidelines

- Write unit tests for all new features
- Aim for >80% code coverage
- Test edge cases and error conditions
- Use descriptive test names

Example test:
```python
def test_greet_with_name():
    assert app.greet("Alice") == "Hello, Alice!"

def test_greet_returns_string():
    result = app.greet("Bob")
    assert isinstance(result, str)
```

## CI/CD Pipeline

Our CI/CD pipeline automatically runs when you create a PR:

1. **Tests** - Run on Python 3.9, 3.10, 3.11, 3.12 across Ubuntu, Windows, macOS
2. **Code Quality** - Flake8, Black, isort checks
3. **Coverage** - Reports to Codecov
4. **Security** - CodeQL analysis

All checks must pass before merging.

## Commit Message Guidelines

Use conventional commits:

```
feat: add new feature
fix: fix a bug
docs: documentation changes
style: code style changes
refactor: refactor code
test: add or update tests
ci: CI/CD changes
```

## Questions or Issues?

- Open an issue for bugs
- Use discussions for feature requests
- Check existing issues before creating new ones

Thank you for contributing! 🎉
