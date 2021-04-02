from modules import header_module
from pages.BasePO import BasePO

class HeaderBO(BasePO):
    def log_out(self):
        self._click_element(header_module.LOGOUT_BTN)
        return self
