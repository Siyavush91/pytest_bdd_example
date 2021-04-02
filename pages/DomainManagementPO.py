from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from pages.BasePO import BasePO

class DomainManagementPO(BasePO):
    TEMPLATES_TAB = (By.XPATH, f"//*[text()='{constants.TEMPLATES_TAB}']")
    REQUIREMENTS_TAB = (By.XPATH, f"//*[text()='{constants.REQUIREMENTS_TAB}']")
    REWARDS_TAB = (By.XPATH, f"//*[text()='{constants.REWARDS_TAB}']")
    MH_GLOBAL_PANEL = (By.XPATH, f"//*[text()='{constants.MH_GLOBAL_PANEL}']")
    MENU_SUBDOMAINS = (By.XPATH, f"//*[text()='{constants.MH_GLOBAL_PANEL}']//following-sibling::div//child::button")
    ADD_TEMPLATE_BTN = (By.CSS_SELECTOR, "[data-id='add-template-btn']")
    ALL_COUNTRIES = (By.XPATH, f"//*[text()='{constants.ALL_COUNTRIES}']")
    TEMPLATES_NUMBER = (By.XPATH, f"//*[text()='{constants.TEMPLATES_NUMBER}']")
    SUBDOMAINS_NUMBER = (By.XPATH, f"//*[text()='{constants.SUBDOMAINS_NUMBER}']")
    NOTIFICATIONS = (By.XPATH, f"//*[text()='{constants.NOTIFICATIONS}']")

    CREATE_SUBDOMAIN = (By.XPATH, f"//*[text()='{constants.CREATE_SUBDOMAIN}']")
    DOMAIN_OPERATOR = (By.XPATH, f"//*[text()='{constants.DOMAIN_OPERATOR}']")
    SUBDOMAIN_INVITES = (By.XPATH, f"//*[text()='{constants.SUBDOMAIN_INVITES}']")
    COPY_DOMAIN_ID = (By.XPATH, f"//*[text()='{constants.COPY_DOMAIN_ID}']")
    DELETE_DOMAIN = (By.XPATH, f"//*[text()='{constants.DELETE_DOMAIN}']")

    TEMPLATES_HEADER = (By.XPATH, f"//*[text()='{constants.TEMPLATES_HEADER}']")
    ACTIVATIONS_HEADER = (By.XPATH, f"//*[text()='{constants.ACTIVATIONS_HEADER}']")
    VIEWS_HEADER = (By.XPATH, f"//*[text()='{constants.VIEWS_HEADER}']")
    
    def waiter(self):
        self._wait_element_displayed(self.ADD_TEMPLATE_BTN)
        return self

    def verify_domain_managment_page(self):
        self._wait_elements_displayed([self.TEMPLATES_TAB, self.REQUIREMENTS_TAB, self.REWARDS_TAB])
        self._wait_elements_displayed([self.NOTIFICATIONS, self.ADD_TEMPLATE_BTN, self.MH_GLOBAL_PANEL, self.MENU_SUBDOMAINS])
        self._wait_elements_displayed([self.ALL_COUNTRIES, self.TEMPLATES_NUMBER, self.SUBDOMAINS_NUMBER])
        # TODO: check search bar
        asserts.soft_assert_equal(self._get_element_text(self.ADD_TEMPLATE_BTN), constants.ADD_TEMPLATE_BTN)
        return self

    def verify_subdomain_menu(self):
        self._wait_elements_displayed([self.CREATE_SUBDOMAIN, self.DOMAIN_OPERATOR, self.SUBDOMAIN_INVITES, self.COPY_DOMAIN_ID, self.DELETE_DOMAIN])
        return self
    
    def verify_domain(self, name):
        self._verify_element_with_text(name)
    
    def verify_added_template(self, name):
        self._wait_elements_displayed([self.TEMPLATES_HEADER, self.ACTIVATIONS_HEADER, self.VIEWS_HEADER])
        self._verify_element_with_text(name)

    def open_subdomain_menu(self):
        self._click_element(self.MENU_SUBDOMAINS)
        return self

    def choose_option(self, option):
        if option == 'Create subdomain':
            self._click_element(self.CREATE_SUBDOMAIN)
        else:
            raise('Unsupported option')

    def click_add_template(self):
        self._click_element(self.ADD_TEMPLATE_BTN)
    
    def click_on_template(self, name):
        locator = (By.XPATH, f"//*[text()='{name}']")
        self._click_element(locator)
