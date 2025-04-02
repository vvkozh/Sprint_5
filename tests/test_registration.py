from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from helpers import generate_email
import data


class TestRegistrationChrome:
    def test_success_registration_chrome(self, driver_chrome_reg):
        # arrange
        email = generate_email()
        driver_chrome_reg.find_element(*Locators.REG_NAME).send_keys(data.NAME)
        driver_chrome_reg.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver_chrome_reg.find_element(*Locators.REG_PASSWORD).send_keys(data.PASSWORD)
        #  act
        driver_chrome_reg.find_element(*Locators.BUT_REG_END).click()
        WebDriverWait(driver_chrome_reg, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_LOGIN, 'Войти'))
        # assert
        assert driver_chrome_reg.current_url == 'https://stellarburgers.nomoreparties.site/login'

class TestRegistrationFirefox:
    def test_success_registration_firefox(self, driver_firefox_reg):
        # arrange
        email = generate_email()
        driver_firefox_reg.find_element(*Locators.REG_NAME).send_keys(data.NAME)
        driver_firefox_reg.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver_firefox_reg.find_element(*Locators.REG_PASSWORD).send_keys(data.PASSWORD)
        #act
        driver_firefox_reg.find_element(*Locators.BUT_REG_END).click()
        WebDriverWait(driver_firefox_reg, 3).until(expected_conditions.text_to_be_present_in_element(Locators.BUT_LOGIN, 'Войти'))
        # assert
        assert driver_firefox_reg.current_url == 'https://stellarburgers.nomoreparties.site/login'

class TestRegistrationWIthInvalidPasswordChrome:
    def test_invalid_registration_chrome(self, driver_chrome_reg):
        # arrange
        email = generate_email()
        driver_chrome_reg.find_element(*Locators.REG_NAME).send_keys(data.NAME)
        driver_chrome_reg.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver_chrome_reg.find_element(*Locators.REG_PASSWORD).send_keys(data.PASSWORD_INVALID)
        # act
        driver_chrome_reg.find_element(*Locators.BUT_REG_END).click()
        invalid_pass_text = WebDriverWait(driver_chrome_reg, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_INVALID_PASSWORD)).text
        # assert
        assert invalid_pass_text == 'Некорректный пароль'

class TestRegistrationWIthInvalidPasswordFirefox:
    def test_invalid_registration_firefox(self, driver_firefox_reg):
        # arrange
        email = generate_email()
        driver_firefox_reg.find_element(*Locators.REG_NAME).send_keys(data.NAME)
        driver_firefox_reg.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver_firefox_reg.find_element(*Locators.REG_PASSWORD).send_keys(data.PASSWORD_INVALID)
        # act
        driver_firefox_reg.find_element(*Locators.BUT_REG_END).click()
        invalid_pass_text = WebDriverWait(driver_firefox_reg, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_INVALID_PASSWORD)).text
        # assert
        assert invalid_pass_text == 'Некорректный пароль'
