# language: pt

Funcionalidade: Autenticação no aplicativo Digi Professores
  Como um professor
  Quero fazer login no aplicativo
  Para acessar as funcionalidades do sistema

  Contexto:
    Dado que o aplicativo está aberto na tela de login

  Cenário: Login com credenciais válidas
    Quando eu aceito os termos e condições
    E eu preencho o CPF "017.201.420-41"
    E eu preencho a senha "12345678Ab"
    E eu clico no botão de login
    E eu clico no botão avançar
    Então eu devo ser redirecionado para a tela inicial

  Cenário: Login com credenciais inválidas
    Quando eu aceito os termos e condições
    E eu preencho o CPF "000.000.000-00"
    E eu preencho a senha "senhaErrada"
    E eu clico no botão de login
    Então eu devo ver uma mensagem de erro