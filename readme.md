# 📊 System Base Data BI

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-5.0%2B-green.svg)](https://www.djangoproject.com/)
[![Package Manager](https://img.shields.io/badge/poetry-1.8%2B-blueviolet.svg)](https://python-poetry.org/)
[![Database](https://img.shields.io/badge/database-PostgreSQL-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/license-MIT-informational.svg)](LICENSE)

O **System Base Data BI** é uma plataforma desenvolvida em **Django** para a gestão centralizada, acompanhamento e auditoria do ciclo de vida de **processos, convênios e projetos de pesquisa, extensão e inovação** (no contexto universitário/institucional, como o ecossistema UnB/SEI).

O sistema foi arquitetado desde a sua modelagem relacional para atuar como **Data Source (Fonte de Dados de Alta Performance)** para relatórios e dashboards no **Power BI**, garantindo dados normalizados, rastreabilidade orçamentária e integridade relacional.

---

## 📌 Principais Funcionalidades

- **Gestão de Processos & Convênios:** Controle de prazos, vigências, números do SEI, termos de adesão e assinaturas.
- **Detalhamento Orçamentário e Financeiro:** Lançamento fracionado do Plano de Despesas (`ItemPlanoDespesa`), distinguindo bolsas, diárias, equipamentos, passagens e serviços de terceiros.
- **Rastreabilidade de Participação Acadêmica:** Vínculo de pessoas a múltiplos papéis (Coordenador, Supervisor Acadêmico, Relator e Substituto).
- **Mapeamento Multisetorial (N:N):** Suporte a múltiplas Unidades Acadêmicas/Administrativas interessadas em um mesmo projeto.
- **Alinhamento Estratégico:** Categorização por Modalidade, Natureza, Esfera Administrativa e Objetivos de Desenvolvimento Sustentável (ODS/ONU).
- **Gerador de Dados de Teste (Management Command):** Script CLI customizado e otimizado para gerar dados sintéticos em alta escala via inserções em lote (`bulk_create`).

---

## 🗺️ Mapeamento de Rotas e Endpoints (URLs)

As rotas da aplicação estão divididas entre o módulo de administração, autenticação e os aplicativos funcionais (`processos` e `pessoas`).

> **⚠️ Nota de Arquitetura de URLs:** As rotas estáticas/específicas (ex: `/unidades/`) são declaradas antes das rotas dinâmicas com parâmetros (ex: `/<int:pk>/`) para evitar sobrescrita no resolvedor do Django.

### 🔹 App `processos` (`/processos/`)

| Método | URL / Rota | View associada | Descrição |
| :--- | :--- | :--- | :--- |
| `GET` | `/processos/` | `ProcessoListView` | Lista paginada de todos os processos/projetos cadastrados. |
| `GET` | `/processos/unidades/` | `UnidadeListView` | Lista de todas as Unidades Acadêmicas/Administrativas. |
| `GET` | `/processos/modalidades/` | `ModalidadeListView` | Lista de modalidades (Pesquisa, Ensino, Extensão, etc.). |
| `GET` | `/processos/naturezas/` | `NaturezaListView` | Lista de naturezas dos projetos (Acadêmico, Tecnológico, etc.). |
| `GET` | `/processos/despesas/` | `ItemPlanoDespesaListView` | Visão consolidada dos itens do plano de despesas. |
| `GET` | `/processos/<int:pk>/` | `ProcessoDetailView` | Detalhes completos de um processo específico por ID. |
| `GET` | `/processos/novo/` | `ProcessoCreateView` | Formulário para cadastro de um novo processo/projeto. |
| `POST`| `/processos/novo/` | `ProcessoCreateView` | Processa a criação e grava o novo processo no banco. |
| `GET` | `/processos/<int:pk>/editar/`| `ProcessoUpdateView` | Form de edição dos dados gerais e financeiros. |
| `POST`| `/processos/<int:pk>/editar/`| `ProcessoUpdateView` | Grava as alterações do processo existente. |
| `POST`| `/processos/<int:pk>/deletar/`| `ProcessoDeleteView` | Remove um processo da base de dados. |

### 🔹 App `pessoas` (`/pessoas/`)

| Método | URL / Rota | View associada | Descrição |
| :--- | :--- | :--- | :--- |
| `GET` | `/pessoas/` | `PessoaListView` | Listagem geral de docentes, técnicos, colaboradores e alunos. |
| `GET` | `/pessoas/<int:pk>/` | `PessoaDetailView` | Exibe o perfil da pessoa e os projetos vinculados a ela. |

### 🔹 Rotas Globais e Sistema

| Método | URL / Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/admin/` | Painel Administrativo nativo do Django (`Django Admin`). |
| `GET` | `/` | Redirecionamento/Dashboard principal do sistema web. |

---

## 🛠️ Tecnologias e Gerenciamento de Pacotes

- **Linguagem:** Python 3.12+
- **Gerenciador de Dependências:** [Poetry](https://python-poetry.org/) (`pyproject.toml` / `poetry.lock`)
- **Framework Web:** Django 5.x
- **Banco de Dados:** PostgreSQL / SQLite (Dev)
- **Driver de Banco:** `psycopg3`
- **Massa de Dados / Testes:** `Faker` (pt_BR)
- **Business Intelligence:** Power BI Desktop / Power BI Service (DirectQuery ou Import via OLE DB/PostgreSQL Connector)

---

## 🚀 Guia de Instalação e Execução Local

### 1. Pré-requisitos
- Python 3.12 ou superior instalado.
- [Poetry](https://python-poetry.org/docs/#installation) instalado no ambiente do sistema.
- PostgreSQL rodando localmente ou via Container Docker.

### 2. Instalação de Dependências com Poetry

```bash
# Clone o repositório
git clone [https://github.com/paulovitorgm/bi.git](https://github.com/paulovitorgm/bi.git)
cd bi

# Instale todas as dependências mapeadas no pyproject.toml
poetry install

# Ative o ambiente virtual criado pelo Poetry
poetry shell