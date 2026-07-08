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
    │   ├── utils/
    │   └── locators/
    │    
    ├── behave.ini
    ├── .gitignore
    ├── README.md   
    ├── DOCKER_README.md 
    └── pyproject.toml    

## ⚙️ Instalação

Após clonar o repositório, sincronize todas as dependências (incluindo as de dev) com:

``` bash
uv sync --all-extras
```

### 🖥️ Iniciar Appium

``` bash
appium
```

### 🖥️ Iniciar Ambiente virtual

``` bash
venv/scripts/activate
```

## OBS: Lembrar de rodar um emulador antes de executar os testes, criar o .env preenchendo com dados de login e ajustar também os capabilities do desired capabilities no arquivo de configuração.

## ▶️ Executando os Testes

O projeto utiliza o **taskipy** para gerenciar os scripts. Todos os comandos seguem o padrão `uv run task <nome>`.

Para listar todos os tasks disponíveis:

``` bash
uv run task --list
```

---

### 🧹 Manutenção

| Comando | Descrição |
|---|---|
| `uv run task clean` | Limpa relatórios e logs antigos |
| `uv run task lint` | Verifica problemas de estilo no código |
| `uv run task format` | Formata automaticamente os arquivos Python |

### 📊 Relatórios

| Comando | Descrição |
|---|---|
| `uv run task report` | Inicia o servidor Allure para visualizar relatórios |

### 🚀 Execução Geral

| Comando | Descrição |
|---|---|
| `uv run task test` | Limpa e executa **todos** os testes |
| `uv run task test-debug` | Executa com saída detalhada (debug) |
| `uv run task test-ci` | Execução compacta para pipelines CI/CD |
| `uv run task test-allure` | Executa e abre o relatório Allure |

### 🎯 Testes por Módulo (Developer Focus)

| Comando | Descrição |
|---|---|
| `uv run task test-login` | Apenas os testes de **Login** |

### 🐳 Execução via Docker (Taskipy)

| Comando | Descrição |
|---|---|
| `uv run task docker-test` | Executa os testes dentro do container Docker |
| `uv run task docker-test-build` | Reconstrói a imagem e executa os testes no Docker |
| `uv run task docker-clean` | Remove containers, volumes e redes criados pelo Docker Compose |


## 📌 Comandos Úteis

### Iniciar Appium

``` bash
appium
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
