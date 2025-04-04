from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
from locators import Locators


class TestLoginViaButtonLoginAccountChrome:
    def test_success_login_via_but_login_account_chrome(self, driver_chrome):
        # arrange
        driver_chrome.find_element(*Locators.BUT_LOGIN_IN_ACCOUNT).click()
        driver_chrome.find_element(*Locators.LOG_EMAIL).send_keys(data.LOGIN_EMAIL)
        driver_chrome.find_element(*Locators.LOG_PASSWORD).send_keys(data.PASSWORD)
        # act
        driver_chrome.find_element(*Locators.BUT_LOGIN).click()
        text_but_order = WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER_PLACE)).text
        # assert
        assert text_but_order == 'Оформить заказ'

class TestLoginViaButtonPersonalAccountChrome:
    def test_success_login_via_but_personal_account_chrome(self, driver_chrome):
        # arrange
        driver_chrome.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
        driver_chrome.find_element(*Locators.LOG_EMAIL).send_keys(data.LOGIN_EMAIL)
        driver_chrome.find_element(*Locators.LOG_PASSWORD).send_keys(data.PASSWORD)
        # act
        driver_chrome.find_element(*Locators.BUT_LOGIN).click()
        text_but_order = WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER_PLACE)).text
        # assert
        assert text_but_order == 'Оформить заказ'

class TestLoginViaButtonRegistrationChrome:
    def test_success_login_via_but_registration_chrome(self, driver_chrome):
        # arrange
        driver_chrome.find_element(*Locators.BUT_LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_REGISTRATION, 'Зарегистрироваться'))
        driver_chrome.find_element(*Locators.BUT_REGISTRATION).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_LOGIN_WHEN_REGISTRATED, 'Войти'))
        driver_chrome.find_element(*Locators.BUT_LOGIN_WHEN_REGISTRATED).click()
        driver_chrome.find_element(*Locators.LOG_EMAIL).send_keys(data.LOGIN_EMAIL)
        driver_chrome.find_element(*Locators.LOG_PASSWORD).send_keys(data.PASSWORD)
        # act
        driver_chrome.find_element(*Locators.BUT_LOGIN).click()
        text_but_order = WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER_PLACE)).text
        # assert
        assert text_but_order == 'Оформить заказ'

class TestLoginViaButtonRecoveryPasswordChrome:
    def test_success_login_via_but_recovery_password_chrome(self, driver_chrome):
        # arrange
        driver_chrome.find_element(*Locators.BUT_LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_RECOVERY_PASSWORD, 'Восстановить пароль'))
        driver_chrome.find_element(*Locators.BUT_RECOVERY_PASSWORD).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_LOGIN_WHEN_REGISTRATED, 'Войти'))
        driver_chrome.find_element(*Locators.BUT_LOGIN_RECOVERY_PASSWORD).click()
        driver_chrome.find_element(*Locators.LOG_EMAIL).send_keys(data.LOGIN_EMAIL)
        driver_chrome.find_element(*Locators.LOG_PASSWORD).send_keys(data.PASSWORD)
        # act
        driver_chrome.find_element(*Locators.BUT_LOGIN).click()
        text_but_order = WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER_PLACE)).text
        # assert
        assert text_but_order == 'Оформить заказ'

class TestLoginViaButtonLoginAccountFirefox:
    def test_success_login_via_but_login_account_firefox(self, driver_firefox):
        # arrange
        driver_firefox.find_element(*Locators.BUT_LOGIN_IN_ACCOUNT).click()
        driver_firefox.find_element(*Locators.LOG_EMAIL).send_keys(data.LOGIN_EMAIL)
        driver_firefox.find_element(*Locators.LOG_PASSWORD).send_keys(data.PASSWORD)
        # act
        driver_firefox.find_element(*Locators.BUT_LOGIN).click()
        text_but_order = WebDriverWait(driver_firefox, 3).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER_PLACE)).text
        # assert
        assert text_but_order == 'Оформить заказ'

class TestLoginViaButtonPersonalAccountFirefox:
    def test_success_login_via_but_personal_account_firefox(self, driver_firefox):
        # arrange
        driver_firefox.find_element(*Locators.BUT_PERSONAL_ACCOUNT).click()
        driver_firefox.find_element(*Locators.LOG_EMAIL).send_keys(data.LOGIN_EMAIL)
        driver_firefox.find_element(*Locators.LOG_PASSWORD).send_keys(data.PASSWORD)
        # act
        driver_firefox.find_element(*Locators.BUT_LOGIN).click()
        text_but_order = WebDriverWait(driver_firefox, 3).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER_PLACE)).text
        # assert
        assert text_but_order == 'Оформить заказ'

class TestLoginViaButtonRegistrationFirefox:
    def test_success_login_via_but_registration_firefox(self, driver_firefox):
        # arrange
        driver_firefox.find_element(*Locators.BUT_LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver_firefox, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_REGISTRATION, 'Зарегистрироваться'))
        driver_firefox.find_element(*Locators.BUT_REGISTRATION).click()
        WebDriverWait(driver_firefox, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_LOGIN_WHEN_REGISTRATED, 'Войти'))
        driver_firefox.find_element(*Locators.BUT_LOGIN_WHEN_REGISTRATED).click()
        driver_firefox.find_element(*Locators.LOG_EMAIL).send_keys(data.LOGIN_EMAIL)
        driver_firefox.find_element(*Locators.LOG_PASSWORD).send_keys(data.PASSWORD)
        # act
        driver_firefox.find_element(*Locators.BUT_LOGIN).click()
        text_but_order = WebDriverWait(driver_firefox, 3).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER_PLACE)).text
        # assert
        assert text_but_order == 'Оформить заказ'

class TestLoginViaButtonRecoveryPasswordFirefox:
    def test_success_login_via_but_recovery_password_firefox(self, driver_firefox):
        # arrange
        driver_firefox.find_element(*Locators.BUT_LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver_firefox, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_RECOVERY_PASSWORD, 'Восстановить пароль'))
        driver_firefox.find_element(*Locators.BUT_RECOVERY_PASSWORD).click()
        WebDriverWait(driver_firefox, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_LOGIN_WHEN_REGISTRATED, 'Войти'))
        driver_firefox.find_element(*Locators.BUT_LOGIN_RECOVERY_PASSWORD).click()
        driver_firefox.find_element(*Locators.LOG_EMAIL).send_keys(data.LOGIN_EMAIL)
        driver_firefox.find_element(*Locators.LOG_PASSWORD).send_keys(data.PASSWORD)
        # act
        driver_firefox.find_element(*Locators.BUT_LOGIN).click()
        text_but_order = WebDriverWait(driver_firefox, 3).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER_PLACE)).text
        # assert
        assert text_but_order == 'Оформить заказ'