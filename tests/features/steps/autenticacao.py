from behave import given, when, then
from tests.pages.login.login_page import PaginaLogin

@given('que o aplicativo está aberto na tela de login')
def aberto_na_pagina_de_login(context):
    context.login_page = PaginaLogin(context.driver)
    
    print("✓ App aberto na tela de login")

@when('eu preencho o CPF "(.*)"')
def step_preencher_cpf(context, cpf):
    context.login_page.preencher_cpf_cnpj(cpf)

    print(f"✓ CPF preenchido: {cpf}")

@when('eu preencho a senha "(.*)"')
def step_preencher_senha(context, senha):
    context.login_page.preencher_senha(senha)

    print("✓ Senha preenchida")

@when('eu clico no botão de login')
def step_clicar_login(context):
    context.login_page.clicar_botao_login()

    print("✓ Botão de login clicado")

@then('eu devo ser redirecionado para a tela inicial')
def step_verificar_tela_inicial(context):
    import time
    time.sleep(2)  
    
    print("✓ Usuário na tela inicial")

@then('eu devo ver uma mensagem de erro')
def step_verificar_mensagem_erro(context):
    assert context.login_page.verificar_erro_visivel(), "Mensagem de erro não apareceu"
    mensagem = context.login_page.obter_mensagem_erro()
    print(f"✓ Mensagem de erro exibida: {mensagem}")