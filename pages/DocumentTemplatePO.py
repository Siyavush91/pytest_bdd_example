from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO
from selenium.webdriver.support.ui import Select
import os, time

class DocumentTemplatePO(BasePO):
    ADD_PHOTO = (By.CLASS_NAME, "img-manager__input")
    NEXT_BTN = (By.XPATH, f"//*[text()='{constants.NEXT_BTN}']")

    def verify_rf_passport_template(self):
        self._verify_elements_with_text([constants.RF_PASSPORT, constants.RF_PASSPORT_LASTNAME, constants.RF_PASSPORT_NAME, constants.RF_PASSPORT_SECOND_NAME, constants.RF_PASSPORT_GENDER])
        self._verify_elements_with_text([constants.RF_PASSPORT_DOB, constants.RF_PASSPORT_POB, constants.RF_PASSPORT_NUMBER, constants.RF_PASSPORT_GIVEN_BY, constants.RF_PASSPORT_GIVEN_WHEN])
        self._verify_elements_with_text([constants.RF_PASSPORT_PHOTO, constants.RF_PASSPORT_PHOTO_DESC, constants.NEXT_BTN])

    def fill_text_field(self, name, value):
        locator = (By.XPATH, f"//*[text()='{name}']//following-sibling::div//descendant::label//descendant::input")
        self._click_element(locator)
        self.driver.find_element(*locator).send_keys(value)

    def select_value(self, name, value):
        locator = (By.XPATH, f"//*[text()='{name}']//following-sibling::div//descendant::select")
        drop = Select(self.driver.find_element(*locator))
        drop.select_by_visible_text(value)

    def add_photo(self):
        self.driver.find_element(*self.ADD_PHOTO).send_keys(os.path.abspath("1.jpeg"))

    def click_next_btn(self):
        self._click_element(self.NEXT_BTN)