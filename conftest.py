import pytest
import data
import curl
from selenium import webdriver
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture
def driver_chrome_reg():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(curl.url_registration)
    yield driver
    driver.quit()

@pytest.fixture
def driver_firefox_reg():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(curl.url_registration)
    yield driver
    driver.quit()

@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(curl.main_site)
    yield driver
    driver.quit()

@pytest.fixture
def driver_firefox():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(curl.main_site)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_account_chrome(driver_chrome):
    driver_chrome.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
    driver_chrome.find_element(*Locators.LOG_EMAIL).send_keys(data.LOGIN_EMAIL)
    driver_chrome.find_element(*Locators.LOG_PASSWORD).send_keys(data.PASSWORD)
    driver_chrome.find_element(*Locators.BUT_LOGIN).click()
    WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER_PLACE))
    return driver_chrome

@pytest.fixture
def login_in_account_firefox(driver_firefox):
    driver_firefox.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
    driver_firefox.find_element(*Locators.LOG_EMAIL).send_keys(data.LOGIN_EMAIL)
    driver_firefox.find_element(*Locators.LOG_PASSWORD).send_keys(data.PASSWORD)
    driver_firefox.find_element(*Locators.BUT_LOGIN).click()
    WebDriverWait(driver_firefox, 3).until(expected_conditions.invisibility_of_element_located(Locators.INVISIBLE_ELEMENT))
    return driver_firefox