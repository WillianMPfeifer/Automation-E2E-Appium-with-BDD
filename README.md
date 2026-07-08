# Template para testes E2E Mobile com Appium

Projeto de testes automatizados mobile utilizando **Appium + Behave
(BDD)** para garantir a qualidade do produto final

## 🛠️ Tecnologias Utilizadas

-   **Python 3.14**
-   **Appium**
-   **Behave**
-   **Selenium WebDriver**
-   **Ruff**
-   **UV**

## 📁 Estrutura do Projeto

    /
    ├── apps/               
    ├── reports/            
    ├── tests/
    │   ├── config/         
    │   ├── features/       
    │   ├── pages/          
    │   └── utils/          
    ├── behave.ini          
    └── pyproject.toml      

## ▶️ Executando os Testes

### Modo Debug

``` bash
uv run behave --format plain --no-capture
```

### Modo CI/CD

``` bash
uv run behave --format progress --no-capture
```

## 📌 Comandos Úteis

### Iniciar Appium

``` bash
appium
```

### Feature específica

``` bash
uv run behave tests/features/login/autenticacao.feature --format plain --no-capture
```

### Por tags

``` bash
uv run behave --tags=@smoke --format plain --no-capture
```

### Relatório HTML

``` bash
uv run behave -f html -o reports/report.html
```

### Allure

``` bash
uv run behave -f allure_behave.formatter:AllureFormatter -o reports/allure
allure serve reports/allure
```

## 📝 Desenvolvimento

### .feature

``` gherkin
Funcionalidade: Autenticação
  Cenário: Login com sucesso
    Dado que estou na tela de login
    Quando eu preencho as credenciais válidas
    Então devo ver a tela inicial
```

### Locators

``` python
from appium.webdriver.common.appiumby import AppiumBy

class LoginLocators:
    INPUT_CPF = (AppiumBy.ID, "com.digi:id/input_cpf")
    BTN_ENTRAR = (AppiumBy.ID, "com.digi:id/btn_entrar")
```

### Page Object

``` python
from tests.pages.base_page import BasePage
from tests.pages.login.locators import LoginLocators

class LoginPage(BasePage):
    def realizar_login(self, cpf, senha):
        self.escrever(LoginLocators.INPUT_CPF, cpf)
        self.clicar(LoginLocators.BTN_ENTRAR)
```

## 🎯 Boas Práticas

-   Usar context.logger.info()
-   Steps simples chamando Pages
-   Não usar lógica de driver nos steps
-   Manter padrão de nomeação
