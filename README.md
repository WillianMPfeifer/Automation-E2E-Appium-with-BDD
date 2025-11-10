# Testes E2E - Digi Pais e Alunos (Mobile)

Projeto de testes automatizados mobile usando Appium + Behave (BDD) para o aplicativo Digi Pais e Alunos.

## 🛠️ Tecnologias

- **Python 3.8+**
- **Appium** - Automação mobile
- **Behave** - Framework BDD
- **Selenium** - WebDriver

## 📁 Estrutura do Projeto

## ▶️ Executando os Testes

### Iniciar Appium Server
```bash
appium
```

### Executar todos os testes
```bash
behave
```

### Executar feature específica
```bash
behave tests/features/login/autenticacao.feature
```

### Executar com tags
```bash
behave --tags=@smoke
behave --tags=@login
```

### Gerar relatório HTML
```bash
behave -f html -o reports/report.html
```

### Gerar relatório Allure
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure
allure serve reports/allure
```

## 📝 Escrevendo Testes

### 1. Criar arquivo .feature
```gherkin
Funcionalidade: Nome da funcionalidade
  
  Cenário: Descrição do cenário
    Dado que estou na tela X
    Quando eu faço Y
    Então devo ver Z
```

### 2. Criar locators
```python
class MinhaTelaLocators:
    ELEMENTO = (AppiumBy.ID, "com.app:id/elemento")
```

### 3. Criar Page Object
```python
class MinhaTelaPOM(CommonFunctions):
    def fazer_acao(self):
        self.click(MinhaTelaLocators.ELEMENTO)
```

### 4. Implementar steps
```python
@when('eu faço uma ação')
def step_fazer_acao(context):
    context.page.fazer_acao()
    context.page.fazer_segunda_acao()
    context.page.fazer_terceira_acao()
```

## 🎯 Boas Práticas

- ✅ Um arquivo `.feature` por funcionalidade
- ✅ Page Objects para cada tela
- ✅ Locators centralizados
- ✅ Steps reutilizáveis em `common_functions.py`
- ✅ Screenshots automáticos em falhas
- ✅ Nomenclatura clara e descritiva

## 📊 Estrutura de Reports

Os relatórios são gerados em:
- `reports/` - Relatórios HTML/JSON
- `reports/screenshots/` - Screenshots de falhas
- `reports/allure/` - Relatórios Allure


## 📚 Documentação Adicional

- [Appium Docs](http://appium.io/docs/en/latest/)
- [Behave Docs](https://behave.readthedocs.io/)
- [Selenium Python Docs](https://selenium-python.readthedocs.io/)