from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

class TestExitAccountChrome:
    def test_success_click_constructor_chrome(self, login_in_account_chrome):
        # act
        login_in_account_chrome.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
        WebDriverWait(login_in_account_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PERSONAL_DATA))
        login_in_account_chrome.find_element(*Locators.BUT_EXIT).click()
        text_login_account = WebDriverWait(login_in_account_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_LOGIN)).text
        # assert
        assert text_login_account == 'Вход'

class TestExitAccountFirefox:
    def test_success_click_constructor_chrome(self, login_in_account_firefox):
        # act
        login_in_account_firefox.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
        WebDriverWait(login_in_account_firefox, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PERSONAL_DATA))
        login_in_account_firefox.find_element(*Locators.BUT_EXIT).click()
        text_login_account = WebDriverWait(login_in_account_firefox, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_LOGIN)).text
        # assert
        assert text_login_account == 'Вход'