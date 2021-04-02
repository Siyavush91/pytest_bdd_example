from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO
import time

class CreateTemplatePO(BasePO):
    TEMPLATES_TAB = (By.XPATH, f"//*[text()='{constants.TEMPLATES_TAB}']")
    REQUIREMENTS_TAB = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_TAB}']")
    REWARDS_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")

    CREATE_TEMPLATE_HEADER = (By.XPATH, f"//*[text()='{constants.CREATE_TEMPLATE_HEADER}']")
    DOC_PROPERTIES_HEADER = (By.XPATH, f"//*[text()='{constants.DOC_PROPERTIES_HEADER}']")
    DOC_NAME_FIELD = (By.XPATH, f"//*[text()='{constants.DOC_NAME_FIELD}']//following-sibling::div//descendant::input")
    CATEGORY_FIELD = (By.XPATH, f"//*[text()='{constants.CATEGORY_FIELD}']//following-sibling::div//descendant::div")
    STATUS_FIELD = (By.XPATH, f"//*[text()='{constants.STATUS_FIELD}']//following-sibling::div//descendant::div")
    TYPE_FIELD = (By.XPATH, f"//*[text()='{constants.TYPE_FIELD}']//following-sibling::div//descendant::div")
    CODE_FIELD = (By.XPATH, f"//*[text()='{constants.CODE_FIELD}']//following-sibling::div//descendant::input")

    DOC_DESCRIPTION_HEADER = (By.XPATH, f"//*[text()='{constants.DOC_DESCRIPTION_HEADER}']")
    DESCRIPTION_FIELD = (By.XPATH, f"//*[text()='{constants.DESCRIPTION_FIELD}']//following-sibling::div//descendant::textarea")
    CREATE_TEMPLATE_BTN = (By.CSS_SELECTOR, "[data-id='template-publish-draft-btn']")
    CREATE_DRAFT_BTN = (By.XPATH, f"//*[text()='{constants.CREATE_DRAFT_BTN}']")
    DELETE_DRAFT_BTN = (By.XPATH, f"//*[text()='{constants.DELETE_DRAFT_BTN}']")

    DOC_FIELDS_HEADER = (By.XPATH, f"//*[text()='{constants.DOC_FIELDS_HEADER}']")
    ADD_FIELD_BTN = (By.XPATH, f"//*[text()='{constants.ADD_FIELD_BTN}']")
    ADD_FIELD_HEADER = (By.XPATH, f"//*[text()='{constants.ADD_FIELD_HEADER}']")
    FIELD_NAME = (By.XPATH, f"//*[text()='{constants.ADD_FIELD_HEADER}']//following-sibling::*//descendant::*[text()='{constants.FIELD_NAME}']//following-sibling::div//descendant::input")
    FIELD_TYPE = (By.XPATH, f"//*[text()='{constants.ADD_FIELD_HEADER}']//following-sibling::*//descendant::*[text()='{constants.FIELD_TYPE}']//following-sibling::div//descendant::div")
    FIELD_DESC = (By.XPATH, f"//*[text()='{constants.ADD_FIELD_HEADER}']//following-sibling::*//descendant::*[text()='{constants.FIELD_DESC}']//following-sibling::div//descendant::textarea")
    FIELD_PAGE = (By.XPATH, f"//*[text()='{constants.FIELD_PAGE}']//following-sibling::div//descendant::input")
    FIELD_CATEGORY = (By.XPATH, f"//*[text()='{constants.FIELD_CATEGORY}']//following-sibling::div//descendant::div")
    FIELD_VALIDATION = (By.XPATH, f"//*[text()='{constants.FIELD_VALIDATION}']//following-sibling::div//descendant::div")
    FIELD_MASK = (By.XPATH, f"//*[text()='{constants.FIELD_MASK}']//following-sibling::div//descendant::input")
    FIELD_NUMBER_OF_SYMBOLS = (By.XPATH, f"//*[text()='{constants.FIELD_NUMBER_OF_SYMBOLS}']//following-sibling::div//descendant::input")
    CANCEL_BTN = (By.CSS_SELECTOR, "[data-id='template-properties-form-cancel-btn']")
    SAVE_BTN = (By.CSS_SELECTOR, "[data-id='template-properties-form-save-btn']")


    def waiter(self):
        self._wait_element_displayed(self.CREATE_TEMPLATE_BTN)
        return self

    def verify_page(self):
        self._wait_elements_displayed([self.TEMPLATES_TAB, self.REQUIREMENTS_TAB, self.REWARDS_TAB])
        self._wait_elements_displayed([self.CREATE_TEMPLATE_HEADER, self.DOC_PROPERTIES_HEADER, self.DOC_DESCRIPTION_HEADER, self.DOC_FIELDS_HEADER])
        self._wait_elements_displayed([self.DOC_NAME_FIELD, self.CATEGORY_FIELD, self.STATUS_FIELD, self.TYPE_FIELD, self.CODE_FIELD])
        self._wait_elements_displayed([self.DESCRIPTION_FIELD, self.CREATE_TEMPLATE_BTN, self.CREATE_DRAFT_BTN, self.DELETE_DRAFT_BTN])
        self._wait_element_displayed(self.ADD_FIELD_BTN)
        asserts.soft_assert_equal(self._get_element_text(self.CREATE_TEMPLATE_BTN), constants.CREATE_TEMPLATE_BTN)
        return self

    def verify_default_values(self):
        status_locator = (By.XPATH, f"//*[text()='{constants.STATUS_FIELD}']//following-sibling::div//descendant::div[text()='{constants.STATUS_FIELD_VERIDIED}']")
        type_locator = (By.XPATH, f"//*[text()='{constants.TYPE_FIELD}']//following-sibling::div//descendant::div[text()='{constants.TYPE_FIELD_NOT_UNIQUE}']")
        self._wait_elements_displayed([status_locator, type_locator])
        return self
    
    def verify_add_field_form(self):
        self._wait_elements_displayed([self.ADD_FIELD_HEADER, self.FIELD_NAME, self.FIELD_TYPE, self.FIELD_DESC])
        self._wait_elements_displayed([self.FIELD_PAGE, self.FIELD_CATEGORY, self.FIELD_VALIDATION, self.FIELD_MASK, self.FIELD_NUMBER_OF_SYMBOLS])
        self._wait_elements_displayed([self.CANCEL_BTN, self.SAVE_BTN])
        asserts.soft_assert_equal(self._get_element_text(self.CANCEL_BTN), constants.CANCEL_BTN)
        asserts.soft_assert_equal(self._get_element_text(self.SAVE_BTN), constants.SAVE_BTN)
        return self
    
    def verify_field(self, text):
        # BUG: UI bug arrow overlaps name
        self._verify_element_with_text(text)

    def fill_doc_name(self, name):
        self.driver.find_element(*self.DOC_NAME_FIELD).send_keys(name)

    def choose_category(self, category):
        self._click_element(self.CATEGORY_FIELD)
        locator = (By.XPATH, f"//*[text()='{category}']")
        self._click_element(locator)

    def select_status(self, with_verification):
        self._click_element(self.STATUS_FIELD)
        if with_verification:
            locator = (By.XPATH, f"//*[text()='{constants.STATUS_FIELD_VERIDIED}']")
        else:
            locator = (By.XPATH, f"//*[text()='{constants.STATUS_FIELD_NOT_VERIDIED}']")
        self._click_element(locator)

    def select_type(self, unique):
        self._click_element(self.TYPE_FIELD)
        if unique:
            locator = (By.XPATH, f"//*[text()='{constants.TYPE_FIELD_UNIQUE}']")
        else:
            locator = (By.XPATH, f"//*[text()='{constants.TYPE_FIELD_NOT_UNIQUE}']")
        self._click_element(locator)

    def fill_description(self, desc):
        self.driver.find_element(*self.DESCRIPTION_FIELD).send_keys(desc)

    def fill_code(self, code):
        self.driver.find_element(*self.CODE_FIELD).send_keys(code)

    def click_add_field(self):
        self._click_element(self.ADD_FIELD_BTN)

    def close_field_form(self):
        self._click_element(self.CANCEL_BTN)

    def save_field_form(self):
        self._click_element(self.SAVE_BTN)

    def add_name_field(self, value):
        self.driver.find_element(*self.FIELD_NAME).send_keys(value)

    def choose_type_of_field(self, field_type):
        self._click_element(self.FIELD_TYPE)
        if field_type == 'Number':
            locator = (By.XPATH, f"//*[text()='{constants.NUMBER}']")
        elif field_type == 'Options':
            locator = (By.XPATH, f"//*[text()='{constants.OPTIONS}']")
        elif field_type == 'Photo':
            locator = (By.XPATH, f"//*[text()='{constants.PHOTO}']")
        else:
            raise('Unsupported type')
        self._click_element(locator)
    
    def click_publish_btn(self):
        self._click_element(self.CREATE_TEMPLATE_BTN)
        time.sleep(5)
    
