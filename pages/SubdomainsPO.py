from selenium.webdriver.common.by import By
from helpers import constants
from pages.BasePO import BasePO

class SubdomainsPO(BasePO):
    RF_PANEL = (By.CSS_SELECTOR, "[data-id='']")#need refactor
    CREATE_SUBDOMAIN_BTN = (By.CSS_SELECTOR, "[data-id='']")#need refactor
    INVITATIONS_BTN = (By.CSS_SELECTOR, "[data-id='']")#need refactor

    # need refactor
    def verify_subdomain_page(self):
        self._wait_elements_displayed([self.RF_PANEL, self.CREATE_SUBDOMAIN_BTN, self.INVITATIONS_BTN])
        self._get_element_text(self.RF_PANEL)
        return self

    def go_to_create_subdomain(self):
        self._click_element(self.CREATE_SUBDOMAIN_BTN)
        return self

    def go_to_invitations(self):
        self._click_element(self.INVITATIONS_BTN)
        return self
