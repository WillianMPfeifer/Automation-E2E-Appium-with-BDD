# Mobile Test Automation Template (Python + Appium + Behave)

Este repositório fornece uma arquitetura base robusta para automação de testes **End-to-End (E2E)** em dispositivos móveis (Android/iOS). O projeto utiliza o padrão de projeto **Page Object Model (POM)** integrado ao desenvolvimento orientado a comportamento (**BDD**).

## 🚀 Tecnologias e Ferramentas

* **Linguagem:** [Python](https://www.python.org/)
* **Driver de Automação:** [Appium](https://appium.io/)
* **Framework BDD:** [Behave](https://behave.readthedocs.io/)
* **Gerenciamento de Pacotes:** [UV](https://github.com/astral-sh/uv) (Alta performance)
* **Code Quality:** [Ruff](https://github.com/astral-sh/ruff)
* **Relatórios:** Allure Report & HTML Formatter

## 📁 Estrutura do Projeto

A arquitetura foi desenhada para ser escalável e de fácil manutenção:

```text
├── apps/                # Binários do aplicativo (.apk / .ipa)
├── reports/             # Artefatos de execução e logs
├── tests/
│   ├── config/          # Capabilities e configurações do driver
│   ├── features/        # Especificações em Gherkin
│   │   └── steps/       # Implementação dos steps (Python)
│   ├── pages/           # Page Objects (Lógica de interação)
│   │   └── locators/    # Seletores de elementos (Separados por tela)
│   └── utils/           # Métodos auxiliares e helpers
├── behave.ini           # Configurações do framework Behave
└── pyproject.toml       # Dependências e configurações do projeto (UV/Ruff)

```

## 🛠️ Configuração e Instalação

1. **Pré-requisitos:**
* Python 3.12+
* Appium Server instalado e configurado.
* Android SDK / Xcode (conforme a plataforma alvo).


2. **Instalação de dependências:**
Este projeto utiliza o `uv` para gestão rápida de pacotes.
```bash
pip install uv
uv sync

```



## ▶️ Execução dos Testes

### Local / Debug

Execução com saída detalhada no console:

```bash
uv run behave --format plain --no-capture

```

### Execução por Tag

Ideal para fumaça (smoke) ou regressão:

```bash
uv run behave --tags=@smoke

```

### Geração de Relatórios

Para gerar e visualizar o relatório **Allure**:

```bash
uv run behave -f allure_behave.formatter:AllureFormatter -o reports/allure
allure serve reports/allure

```

## 📝 Padrões de Desenvolvimento

Para manter a consistência do template, siga estas diretrizes:

* **Page Objects:** Toda interação com a interface deve estar encapsulada em uma classe dentro de `tests/pages`.
* **Locators:** Não utilize seletores hardcoded nos métodos. Mantenha-os em arquivos de `locators` separados para facilitar a manutenção.
* **Hooks:** Utilize o `environment.py` para setup e teardown global (ex: abrir/fechar driver).
* **Clean Code:** O projeto utiliza o **Ruff** para garantir que o código siga o PEP8.

---

> **Nota:** Este é um projeto template. Para utilizá-lo em um contexto real, adicione o arquivo `.apk` ou `.app` na pasta `/apps` e configure as `capabilities` em `tests/config`.

---
