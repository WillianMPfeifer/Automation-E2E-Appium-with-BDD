from tests.pages.common_functions import CommonFunctions
from tests.locators.login.autenticacao import LoginLocators

class PaginaLogin(CommonFunctions):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators
    
    def aceitar_termos(self):
        self.click(self.locators.ACCEPT_TERMS_BUTTON)

    def preencher_cpf_cnpj(self, cpf_cnpj):
        self.send_keys(self.locators.CPF_CNPJ_INPUT, cpf_cnpj)
    
    def preencher_senha(self, senha):
        self.send_keys(self.locators.PASSWORD_INPUT, senha)
    
    def clicar_botao_login(self):
        self.click(self.locators.LOGIN_BUTTON)
        self.hide_keyboard()
    
    def fazer_login(self, cpf_cnpj, senha):
        self.preencher_cpf_cnpj(cpf_cnpj)
        self.preencher_senha(senha)
        self.clicar_botao_login()
    
    def verificar_erro_visivel(self):
        return self.is_element_visible(self.locators.ERROR_MESSAGE, timeout=5)
    
    def obter_mensagem_erro(self):
        if self.verificar_erro_visivel():
            return self.get_text(self.locators.ERROR_MESSAGE)
        return None