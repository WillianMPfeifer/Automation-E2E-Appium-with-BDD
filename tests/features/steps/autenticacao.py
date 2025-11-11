from behave import given, when, then
from tests.pages.login.login_page import LoginPage

@given('que o aplicativo está aberto na tela de login')
def step_app_open_on_login_page(context):
    context.login_page = LoginPage(context.driver)
    
    print("✓ App aberto na tela de login")

@when('eu aceito os termos e condições')
def step_accept_terms(context):
    context.login_page.accept_terms_and_enter()

    print("✓ Termos e condições aceitos")

@when('eu preencho o CPF "{cpf_cnpj}"')
def step_fill_cpf(context, cpf_cnpj):
    context.login_page.fill_cpf_cnpj(cpf_cnpj)

    print("✓ CPF preenchido")

@when('eu preencho a senha "{password}"')
def step_fill_password(context, password):
    context.login_page.fill_password(password)

    print("✓ Senha preenchida")

@when('eu clico no botão de login')
def step_click_login_button(context):
    context.login_page.click_login_button()

    print("✓ Botão de login clicado")

@when('eu clico no botão continuar')
def step_click_continue_button(context):
    context.login_page.click_continue_button() 
    
    print("✓ Botão 'Continuar' clicado")

@then('eu devo ser redirecionado para a tela inicial')
def step_verify_home_screen(context):
    is_visible = context.login_page.verify_home_page()
    assert is_visible, "A tela inicial não foi encontrada!"

    print("✓ Usuário na tela inicial")

@then('eu devo ver uma mensagem de erro')
def step_verify_error_message(context):
    assert context.login_page.verify_error_visible(), "Mensagem de erro não apareceu"
    message = context.login_page.get_error_message()

    print(f"✓ Mensagem de erro exibida: {message}")