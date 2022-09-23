import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="../chromedriver.exe")
    driver.maximize_window()
    yield driver
    driver.quit()
