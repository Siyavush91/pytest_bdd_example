from selenium.webdriver.common.by import By

from . import logger, asserts, constants
from pages.BasePO import BasePO
import time

class NicknameFormPO(BasePO):
    BRAND_HEADER = (By.CLASS_NAME, "auth-container__brand")
    FORM_HEADER = (By.CLASS_NAME, "registration__header")
    FORM_DESC = (By.CLASS_NAME, "registration__description")
    NICKNAME_LABEL = (By.CLASS_NAME, "registration__form-field__label")
    NICKNAME_FLD = (By.CSS_SELECTOR, "[data-id='invite-employee-form-nickname']")
    ADDRESS_LABEL = (By.XPATH, f"//*[text()='{constants.ADDRESS_LABEL}']")
    ADDRESS_FIELD = (By.CSS_SELECTOR, "[data-id='invite-employee-form-address']")
    PHONE_LABEL = (By.XPATH, f"//*[text()='{constants.PHONE_LABEL}']")
    PHONE_FIELD = (By.CSS_SELECTOR, "[data-id='invite-employee-form-phone']")
    PHOTO_LABEL = (By.CLASS_NAME, "registration__photo__label")
    PHOTO_DROP_ZONE = (By.CLASS_NAME, "registration__photo__dropzone-container")
    PHOTO_CHOOSE_BUTTON = (By.CLASS_NAME, "registration__photo__pick")
    REGISTRATION_BTN = (By.CSS_SELECTOR, "[data-id='invite-employee-form-submit-button']")

    def verify_page(self):
        self._wait_elements_displayed([self.BRAND_HEADER, self.FORM_HEADER, self.FORM_DESC, self.NICKNAME_LABEL, self.NICKNAME_FLD])
        self._wait_elements_displayed([self.PHOTO_LABEL, self.PHOTO_DROP_ZONE, self.PHOTO_CHOOSE_BUTTON, self.REGISTRATION_BTN])
        asserts.soft_assert_equal(self._get_element_text(self.BRAND_HEADER), constants.MIDHUB_NAME)
        asserts.soft_assert_equal(self._get_element_text(self.FORM_HEADER), constants.NICKNAME_FORM_HEADER)
        asserts.soft_assert_equal(self._get_element_text(self.FORM_DESC), constants.NICKNAME_FORM_DESC)
        asserts.soft_assert_equal(self._get_element_text(self.NICKNAME_LABEL), constants.NICKNAME_LABEL)
        asserts.soft_assert_equal(self._get_element_text(self.PHOTO_LABEL), constants.PHOTO_LABEL)
        asserts.soft_assert_equal(self._get_element_text(self.PHOTO_CHOOSE_BUTTON), constants.PHOTO_CHOOSE_BUTTON)
        asserts.soft_assert_equal(self._get_element_text(self.REGISTRATION_BTN), constants.REGISTRATION_BTN)
        return self
    
    def verify_additional_fields(self):
        self._wait_elements_displayed([self.ADDRESS_LABEL, self.ADDRESS_FIELD, self.PHONE_LABEL, self.PHONE_FIELD])
        return self

    def fill_nickname(self):
        self.driver.find_element(*self.NICKNAME_FLD).send_keys("NICK")
        return self

    def fill_address(self):
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys("Спб, Ленина 1")
        return self

    def fill_phone(self):
        self.driver.find_element(*self.PHONE_FIELD).send_keys("+79213333333")
        return self

    def upload_photo(self):
        self.driver.find_element(*self.PHOTO_CHOOSE_BUTTON).send_keys("1.jpeg")
        return self

    def finish_registration(self):
        self._is_element_enabled(*self.REGISTRATION_BTN)
        self._click_element(self.REGISTRATION_BTN)
        return self
