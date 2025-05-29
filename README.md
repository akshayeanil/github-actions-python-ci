# 🌤️ Weather App (Python)

This is a simple **Python CLI weather application** that retrieves the weather for a given city using the `requests` module. This project demonstrates modern DevOps practices using **GitHub Actions** for Continuous Integration (CI).

---

## 📦 Features

- Fetch current weather data for any city (mocked or actual API can be integrated)
- Simple and testable Python functions
- Integrated **unit testing**
- Automated **code linting** using `flake8`
- Secure use of **GitHub Secrets** and **Repository Variables**

---

## 🛠️ Tech Stack

- **Python 3.11**
- `requests`, `unittest`
- GitHub Actions for CI
- `flake8` for linting and style checks

---

## 🚀 CI/CD Workflow

This project includes a GitHub Actions workflow that:

- Checks out the repository
- Sets up Python 3.11
- Installs dependencies from `requirements.txt`
- Runs unit tests in `/tests`
- Runs `flake8` to check for PEP8 compliance
- Uses GitHub Secrets and Variables securely

---

## 📁 Project Structure

```bash
.
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── weather.py
├── tests/
│   └── test_weather.py
├── requirements.txt
└── README.md
