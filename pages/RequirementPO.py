from . import logger, asserts, constants
from selenium.webdriver.common.by import By
from pages.BasePO import BasePO
import time

class RequirementPO(BasePO):
    TEMPLATES_TAB = (By.XPATH, f"//*[text()='{constants.TEMPLATES_TAB}']")
    REQUIREMENTS_TAB = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_TAB}']")
    REWARDS_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")

    REQUIREMENT_NAME_FIELD_LOCATOR = f"//*[text()='{constants.FIELD_NAME}']//following-sibling::div//descendant::div"
    REQUIREMENT_DOMAINS_FIELD_LOCATOR = f"//*[text()='{constants.REQUIREMENTS_TABLE_DOMAIN}']//following-sibling::div//descendant::div"
    REQUIREMENT_DESC_FIELD_LOCATOR = f"//*[text()='{constants.DESCRIPTION_FIELD}']//following-sibling::div//descendant::div"
    REQUIREMENT_TYPE_FIELD_LOCATOR = f"//*[text()='{constants.REQUIREMENT_TYPE_LABEL}']//following-sibling::div//descendant::div"
    REQUIREMENT_VALIDATORS_LABEL_LOCATOR = f"//*[text()='{constants.REQUIREMENT_VALIDATORS_LABEL}']"
    VALIDATORS_LEVEL_FIELD_LOCATOR = f"//*[text()='{constants.VALIDATORS_LEVEL_LABEL}']//following-sibling::div//descendant::*"
    DOCS_FIELD_LOCATOR = f"//*[text()='{constants.DOCS_LABEL}']//following-sibling::div"

    REQUIREMENT_NAME_FIELD = (By.XPATH, REQUIREMENT_NAME_FIELD_LOCATOR)
    REQUIREMENT_DOMAINS_FIELD = (By.XPATH, REQUIREMENT_DOMAINS_FIELD_LOCATOR)
    REQUIREMENT_DESC_FIELD = (By.XPATH, REQUIREMENT_DESC_FIELD_LOCATOR)
    REQUIREMENT_TYPE_FIELD = (By.XPATH, REQUIREMENT_TYPE_FIELD_LOCATOR)
    REQUIREMENT_VALIDATORS_LABEL = (By.XPATH, REQUIREMENT_VALIDATORS_LABEL_LOCATOR)
    VALIDATORS_LEVEL_FIELD = (By.XPATH, VALIDATORS_LEVEL_FIELD_LOCATOR)
    DOCS_FIELD = (By.XPATH, DOCS_FIELD_LOCATOR)
    EDIT_BTN = (By.XPATH, f"//*[text()='{constants.EDIT_BTN}']")

    def waiter(self):
        self._wait_for_element_present(self.EDIT_BTN)
        return self
    
    def verify_page(self):
        self._wait_elements_displayed([self.TEMPLATES_TAB, self.REQUIREMENTS_TAB, self.REWARDS_TAB])
        self._wait_elements_displayed([self.REQUIREMENT_NAME_FIELD, self.REQUIREMENT_DOMAINS_FIELD, self.REQUIREMENT_DESC_FIELD, self.REQUIREMENT_TYPE_FIELD])
        self._wait_elements_displayed([self.VALIDATORS_LEVEL_FIELD, self.DOCS_FIELD, self.EDIT_BTN])
        return self

    def verify_requirement_name(self, name):
        locator = (By.XPATH, f"{self.REQUIREMENT_NAME_FIELD_LOCATOR}" + f"[text()='{name}']")
        self._wait_element_displayed(locator)

    def verify_requirement_desc(self, desc):
        locator = (By.XPATH, f"{self.REQUIREMENT_DESC_FIELD_LOCATOR}" + f"[text()='{desc}']")
        self._wait_element_displayed(locator)

    def verify_domain(self, domain):
        locator = (By.XPATH, f"{self.REQUIREMENT_DOMAINS_FIELD_LOCATOR}" + f"[text()='{domain}']")
        self._wait_element_displayed(locator)

    def verify_verification_type(self, verification_type):
        locator = (By.XPATH, f"{self.REQUIREMENT_TYPE_FIELD_LOCATOR}" + f"[text()='{verification_type}']")
        self._wait_element_displayed(locator)

    def verify_docs_type(self, docs_type):
        locator = (By.XPATH, f"{self.VALIDATORS_LEVEL_FIELD_LOCATOR}" + f"[text()='{docs_type}']")
        self._wait_element_displayed(locator)

    def verify_doc(self, doc):
        locator = (By.XPATH, f"{self.DOCS_FIELD_LOCATOR}" + f"[text()='{doc}']")
        self._wait_element_displayed(locator)

    





