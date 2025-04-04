from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators

class TestClickChapterRollsChrome:
    def test_success_click_rolls_chrome(self, driver_chrome):
        # arrange
        driver_chrome.find_element(*Locators.BUT_CHAPTER_SAUCES).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BUT_CHAPTER_SAUCES, 'class', 'tab_tab_type_current__2BEPc'))
        # act
        driver_chrome.find_element(*Locators.BUT_CHAPTER_ROLLS).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BUT_CHAPTER_ROLLS, 'class', 'tab_tab_type_current__2BEPc'))
        # assert
        assert 'tab_tab_type_current__2BEPc' in driver_chrome.find_element(*Locators.BUT_CHAPTER_ROLLS).get_attribute("class")

class TestClickChapterSaucesChrome:
    def test_success_click_sauces_chrome(self, driver_chrome):
        # act
        driver_chrome.find_element(*Locators.BUT_CHAPTER_SAUCES).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BUT_CHAPTER_SAUCES, 'class', 'tab_tab_type_current__2BEPc'))
        # assert
        assert 'tab_tab_type_current__2BEPc' in driver_chrome.find_element(*Locators.BUT_CHAPTER_SAUCES).get_attribute("class")

class TestClickChapterFillingsChrome:
    def test_success_click_fillings_chrome(self, driver_chrome):
        # act
        driver_chrome.find_element(*Locators.BUT_CHAPTER_FILLINGS).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BUT_CHAPTER_FILLINGS, 'class', 'tab_tab_type_current__2BEPc'))
        # assert
        assert 'tab_tab_type_current__2BEPc' in driver_chrome.find_element(*Locators.BUT_CHAPTER_FILLINGS).get_attribute("class")

class TestClickChapterRollsFirefox:
    def test_success_click_rolls_chrome(self, driver_firefox):
        # arrange
        driver_firefox.find_element(*Locators.BUT_CHAPTER_SAUCES).click()
        WebDriverWait(driver_firefox, 3).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BUT_CHAPTER_SAUCES, 'class', 'tab_tab_type_current__2BEPc'))
        # act
        driver_firefox.find_element(*Locators.BUT_CHAPTER_ROLLS).click()
        WebDriverWait(driver_firefox, 3).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BUT_CHAPTER_ROLLS, 'class', 'tab_tab_type_current__2BEPc'))
        # assert
        assert 'tab_tab_type_current__2BEPc' in driver_firefox.find_element(*Locators.BUT_CHAPTER_ROLLS).get_attribute("class")

class TestClickChapterSaucesFirefox:
    def test_success_click_sauces_chrome(self, driver_firefox):
        # act
        driver_firefox.find_element(*Locators.BUT_CHAPTER_SAUCES).click()
        WebDriverWait(driver_firefox, 3).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BUT_CHAPTER_SAUCES, 'class', 'tab_tab_type_current__2BEPc'))
        # assert
        assert 'tab_tab_type_current__2BEPc' in driver_firefox.find_element(*Locators.BUT_CHAPTER_SAUCES).get_attribute("class")

class TestClickChapterFillingsFirefox:
    def test_success_click_fillings_chrome(self, driver_firefox):
        # act
        driver_firefox.find_element(*Locators.BUT_CHAPTER_FILLINGS).click()
        WebDriverWait(driver_firefox, 3).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BUT_CHAPTER_FILLINGS, 'class', 'tab_tab_type_current__2BEPc'))
        # assert
        assert 'tab_tab_type_current__2BEPc' in driver_firefox.find_element(*Locators.BUT_CHAPTER_FILLINGS).get_attribute("class")