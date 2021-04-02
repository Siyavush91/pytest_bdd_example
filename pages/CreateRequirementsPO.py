from . import logger, asserts, constants
from selenium.webdriver.common.by import By
from pages.BasePO import BasePO
import time

class CreateRequirementsPO(BasePO):
    TEMPLATES_TAB = (By.XPATH, f"//*[text()='{constants.TEMPLATES_TAB}']")
    REQUIREMENTS_TAB = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_TAB}']")
    REWARDS_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")

    CREATE_REQUIREMENT_HEADER = (By.XPATH, f"//*[text()='{constants.CREATE_REQUIREMENT_HEADER}']")
    REQUIREMENT_NAME_FIELD = (By.XPATH, f"//*[text()='{constants.FIELD_NAME}']//following-sibling::div//descendant::input")
    REQUIREMENT_DOMAINS_FIELD = (By.XPATH, f"//*[text()='{constants.DOMAINS_HEADER}']//following-sibling::div")
    REQUIREMENT_DESC_FIELD = (By.XPATH, f"//*[text()='{constants.DESCRIPTION_FIELD}']//following-sibling::div//descendant::textarea")
    REQUIREMENT_TYPE_LABEL = (By.XPATH, f"//*[text()='{constants.REQUIREMENT_TYPE_LABEL}']")
    REQUIREMENT_VALIDATORS_LABEL = (By.XPATH, f"//*[text()='{constants.REQUIREMENT_VALIDATORS_LABEL}']")
    CHOOSE_VALIDATORS_LEVEL_LABEL = (By.XPATH, f"//*[text()='{constants.CHOOSE_VALIDATORS_LEVEL_LABEL}']")
    CHOOSE_VALIDATORS_HEADER_YELLOW = (By.XPATH, f"//*[text()='{constants.REQUIREMENT_TYPE_LABEL}']//parent::td//following-sibling::td//descendant::div[text()='{constants.YELLOW}']")
    CHOOSE_VALIDATORS_HEADER_GREEN = (By.XPATH, f"//*[text()='{constants.YELLOW}']//ancestor::td//following-sibling::td//descendant::div[text()='{constants.GREEN}']")
    CHOOSE_DOCS_LABEL = (By.XPATH, f"//*[text()='{constants.CHOOSE_DOCS_LABEL}']")
    ADD_DOCS_BTN = (By.XPATH, f"//*[text()='{constants.ADD_DOCUMENT_BTN}']")
    SEARCH_DOC_FIELD = (By.XPATH, f"//*[@placeholder='{constants.SEARCH_DOC_FIELD}']")
    CHOOSE_DOCS_BTN = (By.XPATH, f"//*[text()='{constants.CHOOSE_BTN}']")
    CANCEL_DOCS_BTN = (By.XPATH, f"//*[text()='{constants.CANCEL_BTN}']")

    CREATE_REQUIREMENT_BTN = (By.CSS_SELECTOR, "[data-id='verification-form-submit']")
    CANCEL_REQUIREMENT_BTN = (By.XPATH, f"//*[text()='{constants.CANCEL_BTN2}']")

    def waiter(self):
        self._wait_for_element_present(self.CREATE_REQUIREMENT_BTN)
        return self
    
    def verify_page(self):
        self._wait_elements_displayed([self.TEMPLATES_TAB, self.REQUIREMENTS_TAB, self.REWARDS_TAB])
        self._wait_elements_displayed([self.CREATE_REQUIREMENT_HEADER, self.REQUIREMENT_NAME_FIELD, self.REQUIREMENT_DOMAINS_FIELD, self.REQUIREMENT_DESC_FIELD, self.REQUIREMENT_TYPE_LABEL])
        self._wait_elements_displayed([self.CHOOSE_VALIDATORS_LEVEL_LABEL, self.CHOOSE_VALIDATORS_HEADER_YELLOW, self.CHOOSE_VALIDATORS_HEADER_GREEN])
        self._wait_elements_displayed([self.ADD_DOCS_BTN, self.CREATE_REQUIREMENT_BTN, self.CANCEL_REQUIREMENT_BTN])
        asserts.soft_assert_equal(self._get_element_text(self.CREATE_REQUIREMENT_BTN), constants.CREATE_REQUIREMENT_BTN)
        return self

    def verify_expanded_doc_section(self):
        self._wait_elements_displayed([self.SEARCH_DOC_FIELD, self.CHOOSE_DOCS_BTN, self.CANCEL_DOCS_BTN])

    def verify_added_doc(self, name):
        self._verify_element_with_text(name)

    def fill_requirement_name(self, name):
        self.driver.find_element(*self.REQUIREMENT_NAME_FIELD).send_keys(name)

    def fill_requirement_desc(self, desc):
        self.driver.find_element(*self.REQUIREMENT_DESC_FIELD).send_keys(desc)

    def choose_requirement_domain(self, domain):
        self._click_element(self.REQUIREMENT_DOMAINS_FIELD)
        locator = (By.XPATH, f"//*[text()='{domain}']")
        self._click_element(locator)

    def choose_requirement_type(self, requirement_type):
        locator = (By.XPATH, f"//*[text()='{requirement_type}']")
        self._click_element(locator)

    def enable_type_checkbox(self, requirement_type):
        if requirement_type == constants.TEST_GLOBAL_YELLOW:
            locator = (By.XPATH, f"//*[text()='{constants.GLOBAL}']//parent::td//following-sibling::td//child::div//child::div")
        elif requirement_type == constants.TEST_GLOBAL_GREEN:
            locator =  (By.XPATH, f"//*[text()='{constants.GLOBAL}']//parent::td//following-sibling::td//following-sibling::td//child::div//child::div")
        else:
            raise('Unsupported type')
        self._click_element(locator)

    def click_add_doc_btn(self):
        self._click_element(self.ADD_DOCS_BTN)

    def expand_docs_section(self, docs_section):
        locator = (By.XPATH, f"//*[text()='{docs_section}']")
        self._click_last_element(locator)

    def enable_doc_checkbox(self, doc):
        locator = (By.XPATH, f"//*[text()='{doc}']")
        self._click_element(locator)

    def click_choose_doc_btn(self):
        self._click_element(self.CHOOSE_DOCS_BTN)

    def click_create_requirement(self):
        self._click_element(self.CREATE_REQUIREMENT_BTN)
        time.sleep(3)

    





