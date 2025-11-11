from tests.pages.common_functions import CommonFunctions
from tests.locators.login.autenticacao import LoginLocators

class LoginPage(CommonFunctions):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators
    
    def accept_terms_and_enter(self):
        self.click(self.locators.ACCEPT_TERMS_CHECKBOX)

        self.click(self.locators.ACCEPT_BUTTON)

    def fill_cpf_cnpj(self, cpf_cnpj):
        self.send_keys(self.locators.CPF_FIELD, cpf_cnpj)
    
    def fill_password(self, password):
        self.send_keys(self.locators.PASSWORD_FIELD, password)
    
    def click_login_button(self):
        self.click(self.locators.LOGIN_BUTTON)
        self.hide_keyboard()
    
    def click_continue_button(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def verify_home_page(self, ):
        return self.is_element_visible(self.locators.HOME_SCREEN_IDENTIFIER, timeout=5)
    
    def verify_error_visible(self):
        return self.is_element_visible(self.locators.ERROR_MESSAGE, timeout=5)
    
    def get_error_message(self):
        if self.verify_error_visible():
            return self.get_text(self.locators.ERROR_MESSAGE)
        return None