from . import logger, asserts, constants
from pages.BasePO import BasePO
from pages.ApplicationFormPO import ApplicationFormPO
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import allure
import time



class ApplicationPO(BasePO):
    """Содержит методы для взаимодействия с элементами страницы 'Обработка заявок'"""

    REGISTRIES_FILTERS = (By.CSS_SELECTOR, "div.applications-request__TitleContainer-sc-1l5hzl4-1.bZASyH > button")
    HIDE_FILTERS = (By.CSS_SELECTOR, "[data-id='hide-filters-button']")
    DOMAIN_SELECTOR = (By.CSS_SELECTOR, "#downshift-0-toggle-button")
    # Вкладка со списком заявок на желтую верификацию
    APP_LIST = (By.CSS_SELECTOR, "div.application__space > div > div")
    BTN_REQUEST = (By.CSS_SELECTOR, "[data-id='request-application-button']")
    ERROR_TOAST = (By.CLASS_NAME, "midhub-toast__content")
    PRELOADER = (By.CLASS_NAME, "applications-request__body__request-view__preloader__img")
    APPLICATION_ITEM = (By.CLASS_NAME, "applications-item__inner-space__right-side__application__id")
    RULES_LINK = (By.XPATH, "//*[text()='Правила обработки заявок']")

    # Вкладка со списком обработанных заявок
    IN_PROCESS_TAB =(By.CSS_SELECTOR, "[data-id='processing-applications']")
    APPROVED_TAB = (By.CSS_SELECTOR, "[data-id='approved-applications-tab']")
    PENDING_TAB = (By.CSS_SELECTOR, "a.sc-hzMMCg.jhQIGd")#TODO rebase locator

    def waiter(self):
        self._wait_for_element_present(self.BTN_REQUEST)
        return self


    def verify_application_request_container(self):
        self._wait_elements_displayed([self.REGISTRIES_FILTERS, self.BTN_REQUEST, self.RULES_LINK])
        return self


    def verify_application(self, app_id):
        # BUG: TODO: create locator for not empty item after bug fix
        # self._wait_for_element_not_present(locator_not_empty) 
        app_id_text = self.slice_app_id(app_id)
        locator = (By.XPATH, f"//*[text()='{app_id_text}']")
        self._wait_for_element_present(locator)
        return self


    def tap_domain_filters_btn(self):
        self._click_element(self.REGISTRIES_FILTERS)#
        return self


    def open_domain_selector(self):
        self._click_element(self.DOMAIN_SELECTOR)
        return self


    def choose_domain(self, domain_name):
        element = (By.XPATH, f"//*[text()='{domain_name}']")
        self._click_element(element)
        return self


    def tap_hide_domains_button(self):
        self._click_element(self.REGISTRIES_FILTERS)
        return self


    def verify_chosen_domain(self, domain_name):
        # TODO: add id to cross-button and verify cross for filter as well
        element = (By.XPATH, f"//*[text()='{domain_name}']")
        self._wait_for_element_present(element)
        return self


    def get_last_application_id(self):
        last_app_from_list = self.driver.find_elements(*self.APPLICATION_ITEM)
        app_id = (last_app_from_list[-1]).text
        return app_id


    def verify_empty_application(self, app_id):
        # BUG: TODO: create locator for not empty item after bug fix
        # self._wait_for_element_not_present(locator_not_empty)
        app_id_text = self.slice_app_id(app_id)
        application = (By.XPATH, f"//*[text()='{app_id_text}']")
        self._wait_for_element_present(application)
        return self


    def click_request_button(self):
        self._click_element(self.BTN_REQUEST)
        return self


    def wait_active_request_button(self):
        self._wait_for_element_not_present(self.PRELOADER)
        return self


    def verify_lack_of_application(self, app_Id):
        element = (By.CSS_SELECTOR, f"[data-id='{app_Id}']")
        end_time = time.time() + 30
        while True:
            if self._is_element_not_visible(*element):
                return True
            time.sleep(3)
            self._update_page()
            if time.time() > end_time:
                break
        raise TimeoutException(f"The application is still on the page")


    def verify_toast(self):
        self._wait_for_element_visible(*self.ERROR_TOAST)
        # INFO: can't get toast text with usual method, added workaround
        toast_with_text = (By.XPATH, f"//*[text()='{constants.NO_APPLICATION_TOAST_TEXT}']")
        self._wait_for_element_present(toast_with_text)
        return self


    def toast_visible(self):
        return self._is_element_visible(*self.ERROR_TOAST)


    def slice_app_id(self, app_id):
        app_id_text = app_id[:4] + '...' + app_id[-4:]
        return app_id_text


    def goto_app_form(self, app_id):
        app_id_text = self.slice_app_id(app_id)
        application = (By.CSS_SELECTOR, f"[data-id='{app_id_text}']") #href="#/applications/application/"
        self._click_element(application)
        self._wait_for_element_not_present(self.APP_LIST)
        return ApplicationFormPO(self.driver)


    def goto_app_approved(self):
        self._click_element(self.IN_PROCESS_TAB)
        self._click_element(self.APPROVED_TAB)
        return self


    def goto_app_on_hold(self):
        self._click_element(self.IN_PROCESS_TAB)
        self._click_element(self.PENDING_TAB)
        return self


