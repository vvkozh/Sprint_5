import curl
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestClickConstructorChrome:
    def test_success_click_constructor_chrome(self, login_in_account_chrome):
        # act
        login_in_account_chrome.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
        WebDriverWait(login_in_account_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PERSONAL_DATA))
        login_in_account_chrome.find_element(*Locators.BUT_CONSTRUCTOR).click()
        WebDriverWait(login_in_account_chrome, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_ORDER_PLACE, 'Оформить заказ'))
        # assert
        assert login_in_account_chrome.current_url == curl.main_site

class TestClickStellarBurgerChrome:
    def test_success_click_stellar_burger_chrome(self, login_in_account_chrome):
        # act
        login_in_account_chrome.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
        WebDriverWait(login_in_account_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PERSONAL_DATA))
        login_in_account_chrome.find_element(*Locators.BUT_STELLAR_BURGERS).click()
        WebDriverWait(login_in_account_chrome, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_ORDER_PLACE, 'Оформить заказ'))
        # assert
        assert login_in_account_chrome.current_url == curl.main_site

class TestClickConstructorFirefox:
    def test_success_click_constructor_chrome(self, login_in_account_chrome):
        # act
        login_in_account_chrome.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
        WebDriverWait(login_in_account_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PERSONAL_DATA))
        login_in_account_chrome.find_element(*Locators.BUT_CONSTRUCTOR).click()
        WebDriverWait(login_in_account_chrome, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_ORDER_PLACE, 'Оформить заказ'))
        # assert
        assert login_in_account_chrome.current_url == curl.main_site

class TestClickStellarBurgerFirefox:
    def test_success_click_stellar_burger_firefox(self, login_in_account_firefox):
        # act
        login_in_account_firefox.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
        WebDriverWait(login_in_account_firefox, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PERSONAL_DATA))
        login_in_account_firefox.find_element(*Locators.BUT_STELLAR_BURGERS).click()
        WebDriverWait(login_in_account_firefox, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_ORDER_PLACE, 'Оформить заказ'))
        # assert
        assert login_in_account_firefox.current_url == curl.main_site

