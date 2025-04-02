from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestClickPersonalAccountChrome:
    def test_success_click_personal_account_chrome(self, login_in_account_chrome):
        # act
        login_in_account_chrome.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
        text_change_personal_data = WebDriverWait(login_in_account_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PERSONAL_DATA)).text
        # assert
        assert text_change_personal_data == 'В этом разделе вы можете изменить свои персональные данные'

class TestClickPersonalAccountFirefox:
    def test_success_click_personal_account_firefox(self, login_in_account_firefox):
        # act
        login_in_account_firefox.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
        text_change_personal_data = WebDriverWait(login_in_account_firefox, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PERSONAL_DATA)).text
        # assert
        assert text_change_personal_data == 'В этом разделе вы можете изменить свои персональные данные'