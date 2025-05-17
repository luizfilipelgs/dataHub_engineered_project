# 🧠 back-dhe

Back-end do projeto `dataHub_engineered_project`, desenvolvido com **FastAPI** e organizado com **Poetry**, **Ruff**, **Taskipy** e **Pytest**.

Este README é voltado para quem deseja **clonar e rodar o projeto**, com instruções diretas e práticas.

---

## 📌 Sobre as ferramentas utilizadas

Este projeto foi construído com base em boas práticas modernas de projetos Python. Abaixo, um resumo das principais ferramentas usadas:

- **Poetry**: gerenciador de dependências e ambientes virtuais. Substitui o uso manual de `venv`, `pip` e `requirements.txt`. Toda a configuração do projeto está centralizada no `pyproject.toml`.

- **Taskipy**: ferramenta para definir comandos reutilizáveis (como `run`, `test`, `lint`) dentro do `pyproject.toml`. Com ela, você executa tarefas com `task <comando>`, de forma clara e padronizada.

- **Ruff**: ferramenta de lint e formatação de código ultra-rápida. Substitui ferramentas tradicionais como `flake8`, `isort`, `pylint` e `black`, mantendo o código limpo e padronizado.

Essas ferramentas já estão todas configuradas — basta rodar `poetry install` para tê-las prontas no seu ambiente virtual.

---

## 📦 Requisitos

* **Python** `>=3.13,<4.0`
* **Poetry**, instalado via [`pipx`](https://pypa.github.io/pipx/):

```bash
pip install pipx
pipx install poetry
```

> A instalação com `pipx` evita conflitos globais de dependência e é a forma recomendada.

---

## ⚙️ Instalação do Projeto

```bash
# Clone o repositório
git clone <url-do-repo>
cd back_DHE

# Configure o Poetry para criar o venv local
poetry config virtualenvs.in-project true

# Instale as dependências
poetry install
```

> Isso criará um ambiente virtual isolado em `.venv/` dentro do projeto.

---

## ▶️ Executando o servidor

```bash
task run
```

Esse comando roda a aplicação com:

```
fastapi dev src/back_dhe/app.py
```

A aplicação estará disponível em:
[http://localhost:8000](http://localhost:8000)

---

## 🧪 Rodando os testes

```bash
task test
```

Esse comando executa:

1. `pre_test` → análise com `ruff check`
2. Testes com Pytest
3. `post_test` → geração do relatório de cobertura em `htmlcov/index.html`

---

## 🎨 Corrigindo e formatando o código

```bash
task format
```

Esse comando executa automaticamente:

* `pre_format` → corrige erros de lint com Ruff
* `format` → aplica a formatação com Ruff Formatter

### Para apenas verificar erros de lint:

```bash
task lint
```

---

## 📁 Estrutura do Projeto

```
back_DHE/
├── .venv/                 # Ambiente virtual local
├── src/
│   └── back_dhe/          # Código-fonte da aplicação FastAPI
├── tests/                 # Testes com Pytest
├── pyproject.toml         # Configuração central (Poetry, Taskipy, Ruff, etc.)
├── README.md              # Este arquivo
```

---

## 🔍 Observações

* O projeto segue a estrutura `src/` para evitar conflitos de importação fora do ambiente virtual.
* Todos os comandos são gerenciados com `taskipy` e estão definidos no `pyproject.toml`.
* Ruff substitui ferramentas como `flake8`, `isort` e `black`, sendo usado para **lint** e **formatação**.

---

## 📚 Referência

Baseado no guia: [FastAPI do Zero — Dunossauro](https://fastapidozero.dunossauro.com/estavel/)

