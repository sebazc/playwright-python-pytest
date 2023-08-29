# playwright-python-pytest
This project is a demonstration of how to set up a simple test automation environment. The tools used are:

* Playwright
* Python
* Pytest
* venv
* pytest-html-reporter

## Test object
The page used for testing purposes is [Polymer Shop](https://shop.polymer-project.org/), an e-commerce site which is part of the repository [awesome-sites-to-test-on](https://github.com/BMayhew/awesome-sites-to-test-on). My appreciation to them for building the website and making it public.

The test cases being automated in this sample can be seen in the following <a href="https://docs.google.com/spreadsheets/d/1Yw4RZhlJadAuDd0H-srGgfOUAO1_9h3NVO88YOhAWUQ/edit#gid=0" target="_blank">test cases sheet</a>.

## Test code approach
The project follows a Page Object Model pattern. On one side, each page has a class containing the elements of the page (locators) and methods for interacting with the elements. On the other side, tests are defined, and each test instantiates the page as needed so to interact with it. Assertions (using playwright "expect" object) are performed in the tests, and only attributes and methods from the page classes are used, thus keeping references to the website within the page classes only.

Additionally, a `conftest.py` file is used for set-up and tear-down purposes, an `environment.ini` file for setting variables, a `pytest.ini` file for setting command options, and a `requirements.txt` file for tracking dependencies within the python virtual environment.

## How to run the tests locally
The following are the steps and commands used for running the tests locally.

1. Clone the repo in your computer: `git clone https://github.com/sebazc/playwright-python-pytest.git`
1. Set up your user name: `git config --local user.name "<user name>"`
1. Set up your user email: `git config --local user.email "<user email>"`
1. In the project folder, create the python virtual environment: `python -m venv venv`
1. If using PowerShell in Windows, in a terminal opened with admin access execute: `set-executionpolicy remotesigned`
1. If using PowerShell in Windows, back in the project folder activate the virtual environment: `venv/Scripts/Activate.ps1`
1. Upgrade pip: `venv/Scripts/python.exe -m pip install --upgrade pip`
1. Install the project dependencies: `pip install -r requirements.txt`
1. Download the browsers to be used by playwright: `playwright install`
1. Run the tests :sunglasses:: `pytest`
1. View the report in the browser: `start assets/reports/pytest_html_report.html`
