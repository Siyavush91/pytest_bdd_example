from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO
import time

class TemplatePO(BasePO):
    TEMPLATES_TAB = (By.XPATH, f"//*[text()='{constants.TEMPLATES_TAB}']")
    REQUIREMENTS_TAB = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_TAB}']")
    REWARDS_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")
    DRAFT_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")
    VOTING_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")
    VALIDATORS_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")
    DOMAINS_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")

    DOC_PROPERTIES_HEADER = (By.XPATH, f"//*[text()='{constants.DOC_PROPERTIES_HEADER}']")
    DOC_NAME_FIELD_LOCATOR = f"//*[text()='{constants.DOC_NAME_FIELD}']//following-sibling::div//descendant::input"
    CATEGORY_FIELD_LOCATOR = f"//*[text()='{constants.CATEGORY_FIELD}']//following-sibling::div//descendant::div"
    STATUS_FIELD_LOCATOR = f"//*[text()='{constants.STATUS_FIELD}']//following-sibling::div//descendant::div"
    TYPE_FIELD_LOCATOR = f"//*[text()='{constants.TYPE_FIELD}']//following-sibling::div//descendant::div"
    CODE_FIELD_LOCATOR = f"//*[text()='{constants.CODE_FIELD}']//following-sibling::div//descendant::input"
    DOC_NAME_FIELD = (By.XPATH, DOC_NAME_FIELD_LOCATOR)
    CATEGORY_FIELD = (By.XPATH, CATEGORY_FIELD_LOCATOR)
    STATUS_FIELD = (By.XPATH, STATUS_FIELD_LOCATOR)
    TYPE_FIELD = (By.XPATH, TYPE_FIELD_LOCATOR)
    CODE_FIELD = (By.XPATH, CODE_FIELD_LOCATOR)

    DOC_DESCRIPTION_HEADER = (By.XPATH, f"//*[text()='{constants.DOC_DESCRIPTION_HEADER}']")
    DESCRIPTION_FIELD_LOCATOR = f"//*[text()='{constants.DESCRIPTION_FIELD}']//following-sibling::div//descendant::textarea"
    DESCRIPTION_FIELD = (By.XPATH, DESCRIPTION_FIELD_LOCATOR)
    CREATE_NEW_DRAFT_BTN = (By.CSS_SELECTOR, "[data-id='template-create-draft-btn']")

    DOC_FIELDS_HEADER = (By.XPATH, f"//*[text()='{constants.DOC_FIELDS_HEADER}']")
    FIELD_NAME_LOCATOR = f"//*[text()='{constants.DOC_FIELDS_HEADER}']//parent::div//parent::div//descendant::*[text()='{constants.FIELD_NAME}']"
    FIELD_TYPE_LOCATOR = f"//*[text()='{constants.DOC_FIELDS_HEADER}']//parent::div//parent::div//descendant::*[text()='{constants.FIELD_TYPE}']"
    FIELD_DESC_LOCATOR = f"//*[text()='{constants.DOC_FIELDS_HEADER}']//parent::div//parent::div//descendant::*[text()='{constants.FIELD_DESC}']"
    FIELD_PAGE_LOCATOR = f"//*[text()='{constants.DOC_FIELDS_HEADER}']//parent::div//parent::div//descendant::*[text()='{constants.FIELD_PAGE}']"
    FIELD_CATEGORY_LOCATOR = f"//*[text()='{constants.DOC_FIELDS_HEADER}']//parent::div//parent::div//descendant::*[text()='{constants.FIELD_CATEGORY}']"
    FIELD_VALIDATION_LOCATOR = f"//*[text()='{constants.DOC_FIELDS_HEADER}']//parent::div//parent::div//descendant::*[text()='{constants.FIELD_VALIDATION}']"
    FIELD_MASK_LOCATOR = f"//*[text()='{constants.DOC_FIELDS_HEADER}']//parent::div//parent::div//descendant::*[text()='{constants.FIELD_MASK}']"
    FIELD_NUMBER_OF_SYMBOLS_LOCATOR = f"//*[text()='{constants.DOC_FIELDS_HEADER}']//parent::div//parent::div//descendant::*[text()='{constants.FIELD_NUMBER_OF_SYMBOLS}']"
    FIELD_OPTIONS_LOCATOR = f"//*[text()='{constants.DOC_FIELDS_HEADER}']//parent::div//parent::div//descendant::*[text()='{constants.FIELD_OPTIONS}']"
    FIELD_NUMBER_OF_PHOTOS_LOCATOR = f"//*[text()='{constants.DOC_FIELDS_HEADER}']//parent::div//parent::div//descendant::*[text()='{constants.FIELD_NUMBER_OF_PHOTOS}']"
    FIELD_NAME = (By.XPATH, FIELD_NAME_LOCATOR)
    FIELD_TYPE = (By.XPATH, FIELD_TYPE_LOCATOR)
    FIELD_DESC = (By.XPATH, FIELD_DESC_LOCATOR)
    FIELD_PAGE = (By.XPATH, FIELD_PAGE_LOCATOR)
    FIELD_CATEGORY = (By.XPATH, FIELD_CATEGORY_LOCATOR)
    FIELD_VALIDATION = (By.XPATH, FIELD_VALIDATION_LOCATOR)
    FIELD_MASK = (By.XPATH, FIELD_MASK_LOCATOR)
    FIELD_NUMBER_OF_SYMBOLS = (By.XPATH, FIELD_NUMBER_OF_SYMBOLS_LOCATOR)
    FIELD_OPTIONS = (By.XPATH, FIELD_OPTIONS_LOCATOR)
    FIELD_NUMBER_OF_PHOTOS = (By.XPATH, FIELD_NUMBER_OF_PHOTOS_LOCATOR)

    REQUIREMENTS_LOCAL_CHECK_HEADER = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_LOCAL_CHECK_HEADER}']")
    REQUIREMENTS_GLOBAL_CHECK_HEADER = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_GLOBAL_CHECK_HEADER}']")
    ADD_REQUIREMENTS_BTN = (By.XPATH, f"//*[text()='{constants.ADD_REQUIREMENTS_BTN}']")


    def waiter(self):
        self._wait_element_displayed(self.CREATE_NEW_DRAFT_BTN)
        return self

    def verify_page(self, template_name):
        self._verify_element_with_text(template_name)
        self._wait_elements_displayed([self.TEMPLATES_TAB, self.REQUIREMENTS_TAB, self.REWARDS_TAB])
        self._wait_elements_displayed([self.DRAFT_TAB, self.VOTING_TAB, self.VALIDATORS_TAB, self.DOMAINS_TAB])
        self._wait_elements_displayed([self.DOC_PROPERTIES_HEADER, self.DOC_DESCRIPTION_HEADER, self.DOC_FIELDS_HEADER])
        self._wait_elements_displayed([self.DOC_NAME_FIELD, self.CATEGORY_FIELD, self.STATUS_FIELD, self.TYPE_FIELD, self.CODE_FIELD])
        self._wait_elements_displayed([self.DESCRIPTION_FIELD, self.CREATE_NEW_DRAFT_BTN])
        self._wait_elements_displayed([self.REQUIREMENTS_LOCAL_CHECK_HEADER, self.REQUIREMENTS_GLOBAL_CHECK_HEADER, self.ADD_REQUIREMENTS_BTN])
        asserts.soft_assert_equal(self._get_element_text(self.CREATE_NEW_DRAFT_BTN), constants.CREATE_NEW_DRAFT_BTN)
        return self

    def verify_template_name(self, name):
        locator = (By.XPATH, f"{self.DOC_NAME_FIELD_LOCATOR}" + f"[@value='{name}']")
        self._wait_element_displayed(locator)

    def verify_template_category(self, category):
        locator = (By.XPATH, f"{self.CATEGORY_FIELD_LOCATOR}" + f"[text()='{category}']")
        self._wait_element_displayed(locator)

    def verify_template_status(self, with_verification):
        if with_verification:
            locator = (By.XPATH, f"{self.STATUS_FIELD_LOCATOR}" + f"[text()='{constants.STATUS_FIELD_VERIDIED}']")
        else:
            locator = (By.XPATH, f"{self.STATUS_FIELD_LOCATOR}" + f"[text()='{constants.STATUS_FIELD_NOT_VERIDIED}']")
        self._wait_element_displayed(locator)

    def verify_template_type(self, unique):
        if unique:
            locator = (By.XPATH, f"{self.TYPE_FIELD_LOCATOR}" + f"[text()='{constants.TYPE_FIELD_UNIQUE}']")
        else:
            locator = (By.XPATH, f"{self.TYPE_FIELD_LOCATOR}" + f"[text()='{constants.TYPE_FIELD_NOT_UNIQUE}']")
        self._wait_element_displayed(locator)
    
    def verify_template_code(self, code):
        locator = (By.XPATH, f"{self.CODE_FIELD_LOCATOR}" + f"[@value='{code}']")
        self._wait_element_displayed(locator)

    def verify_template_desc(self, desc):
        locator = (By.XPATH, f"{self.DESCRIPTION_FIELD_LOCATOR}" + f"[text()='{desc}']")
        self._wait_element_displayed(locator)

    def verify_text_field(self, name):
        self._wait_elements_displayed([self.FIELD_NAME, self.FIELD_TYPE, self.FIELD_DESC, self.FIELD_PAGE])
        self._wait_elements_displayed([self.FIELD_CATEGORY, self.FIELD_VALIDATION, self.FIELD_MASK, self.FIELD_NUMBER_OF_SYMBOLS])
        field_name_value = (By.XPATH, f"{self.FIELD_NAME_LOCATOR}" + "//following-sibling::div")
        field_type_value = (By.XPATH, f"{self.FIELD_TYPE_LOCATOR}" + "//following-sibling::div")
        asserts.assert_equal(self._get_element_text(field_name_value), name)
        asserts.assert_equal(self._get_element_text(field_type_value), constants.TEXT)

    def verify_number_field(self, name):
        self._wait_elements_displayed([self.FIELD_NAME, self.FIELD_TYPE, self.FIELD_DESC, self.FIELD_PAGE, self.FIELD_CATEGORY])
        field_name_value = (By.XPATH, f"{self.FIELD_NAME_LOCATOR}" + "//following-sibling::div")
        field_type_value = (By.XPATH, f"{self.FIELD_TYPE_LOCATOR}" + "//following-sibling::div")
        asserts.assert_equal(self._get_element_text(field_name_value), name)
        asserts.assert_equal(self._get_element_text(field_type_value), constants.NUMBER)

    def verify_option_field(self, name):
        self._wait_elements_displayed([self.FIELD_NAME, self.FIELD_TYPE, self.FIELD_DESC, self.FIELD_PAGE, self.FIELD_CATEGORY, self.FIELD_OPTIONS])
        field_name_value = (By.XPATH, f"{self.FIELD_NAME_LOCATOR}" + "//following-sibling::div")
        field_type_value = (By.XPATH, f"{self.FIELD_TYPE_LOCATOR}" + "//following-sibling::div")
        asserts.assert_equal(self._get_element_text(field_name_value), name)
        asserts.assert_equal(self._get_element_text(field_type_value), constants.OPTIONS)

    def verify_photo_field(self, name):
        self._wait_elements_displayed([self.FIELD_NAME, self.FIELD_TYPE, self.FIELD_DESC, self.FIELD_PAGE, self.FIELD_CATEGORY, self.FIELD_NUMBER_OF_PHOTOS])
        field_name_value = (By.XPATH, f"{self.FIELD_NAME_LOCATOR}" + "//following-sibling::div")
        field_type_value = (By.XPATH, f"{self.FIELD_TYPE_LOCATOR}" + "//following-sibling::div")
        asserts.assert_equal(self._get_element_text(field_name_value), name)
        asserts.assert_equal(self._get_element_text(field_type_value), constants.PHOTO)

    def click_field(self, name):
        locator = (By.XPATH, f"//*[text()='{name}']")
        self._click_element(locator)
    
