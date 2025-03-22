import os

import pytest
from selene import browser

from models.student import Student


@pytest.fixture(scope='session', autouse=True)
def setup_browser():
    browser.driver.maximize_window()
    yield
    browser.quit()


@pytest.fixture(scope="function", autouse=True)
def student():
    return Student(
        first_name="John",
        last_name="Doe",
        gender="Male",
        email="john.doe@example.com",
        mobile_number="1234567890",
        birth_date="01 January 2000",
        subjects=["Physics", "Maths", "Computer Science"],
        hobbies=("Sports", "Reading", "Music"),
        picture=os.path.join(os.path.dirname(__file__), "resources", "image.png"),
        address="Some address",
        state="NCR",
        city="Delhi"
    )
