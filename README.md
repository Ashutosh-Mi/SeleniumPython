# 🚀 Selenium Automation Framework (Python + Pytest)

## 📌 Overview

This project is a scalable Selenium automation framework built using Python and Pytest.

It follows industry best practices like Page Object Model (POM), Driver Factory, and Data-Driven Testing.

---

## 🧱 Framework Architecture

tests → conftest → driver factory → config → browser

↓

page objects → base page → selenium actions

---

## 🔧 Tech Stack

* Python
* Pytest
* Selenium WebDriver
* WebDriver Manager
* Allure Reporting
* GitHub Actions (CI/CD)

---

## ✨ Features

* ✅ Page Object Model (POM)
* ✅ Base Page abstraction
* ✅ Driver Factory (dynamic browser handling)
* ✅ Config-driven execution
* ✅ Data-driven testing (JSON)
* ✅ Logging (custom logger)
* ✅ Screenshot capture on failure
* ✅ Retry mechanism for flaky tests
* ✅ Parallel execution (pytest-xdist)
* ✅ CI/CD integration using GitHub Actions

---

## 📁 Project Structure

selenium_framework/

│

├── config/

├── drivers/

├── pages/

├── utils/

├── tests/

├── testdata/

├── logs/

├── screenshots/

├── conftest.py

---

## ▶️ How to Run Tests

### Run all tests

pytest -v

### Run in parallel

pytest -n 2

### Run with Allure report

pytest --alluredir=allure-results
allure serve allure-results

---

## 🔁 CI/CD

This framework is integrated with GitHub Actions:

* Runs automatically on every push
* Executes tests in headless mode
* Uploads logs and screenshots as artifacts

---

## 🧠 Key Concepts Implemented

* Separation of concerns
* Reusability and scalability
* Maintainable test design
* Automated execution pipeline

---

## 📌 Future Enhancements

* Multi-browser matrix execution
* Docker integration
* Cloud execution (Selenium Grid)
* Slack/email notifications

---

## 👨‍💻 Author

[Ashutosh Mishra]
