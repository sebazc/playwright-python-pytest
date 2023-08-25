import pytest
from playwright.sync_api import Page
from configparser import ConfigParser

@pytest.fixture(autouse=True)
def set_up(page: Page):
    config = ConfigParser()
    config.read('environment.ini')

    page.goto(config['parameters']['url'])
    yield
    page.close()