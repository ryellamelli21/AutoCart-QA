# AutoCart-QA Automation Framework

Modern end-to-end Selenium automation framework built using Python and industry-standard QA practices.

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Pytest-xdist (Parallel Testing)
- HTML Reports
- Allure Reports
- GitHub Actions CI/CD
- Docker + Selenium Grid
- Cross-browser Testing (Chrome + Firefox)

---

## Key Features

- Scalable Page Object Model architecture
- Cross-browser automation support
- Parallel execution using pytest-xdist
- Screenshot capture on test failures
- HTML and Allure reporting
- Login validation testing:
  - Invalid credentials
  - Empty fields
  - SQL Injection
  - XSS validation
- Cart functionality testing
- Checkout flow testing
- Logout functionality testing
- CI/CD pipeline integration
- Dockerized Selenium Grid support

---

## Project Structure

```text
AutoCart-QA/
├── tests/                      # Test cases
│   ├── test_login.py
│   ├── test_login_validations.py
│   ├── test_cart.py
│   ├── test_cart_extended.py
│   ├── test_checkout.py
│   └── test_logout.py
│
├── pages/                      # Page Object classes
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── utils/                      # Driver factory
│   └── driver_factory.py
│
├── config/                     # Configurations
│   └── config.py
│
├── reports/                    # HTML reports
├── screenshots/                # Failure screenshots
├── allure-results/             # Allure raw data
├── .github/workflows/          # GitHub Actions
├── conftest.py                 # Fixtures
├── pytest.ini                  # Pytest config
├── requirements.txt
└── README.md