from selenium.webdriver.common.by import By
from . import logger, asserts, constants
from modules import side_menu_module
from pages.BasePO import BasePO

class SideMenuBO(BasePO):
    def go_to_connect_partners(self):
        self._click_element(side_menu_module.PARTNERS)
        return self

    def go_to_domains(self):
        self._click_element(side_menu_module.DOMAINS)
        return self

    def go_to_team_management(self):
        self._click_element(side_menu_module.TEAM_MANAGEMENT)
        return self

    def go_to_company_documents(self):
        self._click_element(side_menu_module.COMPANY_DOCUMENTS)
        return self

    def go_to_admin(self):
        self._click_element(side_menu_module.MENU_ADMIN_SWITCHER)
        return self

    def go_to_work(self):
        self._click_element(side_menu_module.MENU_WORK_SWITCHER)
        return self