# APIcultura

## Desenvolvimento de API REST com FastAPI, Docker, e PostgreSQL

## 1. Descrição do projeto

Esta é uma API genérica, criada com base em um "ToDo Manager", um gerenciador de tarefas, mas feita para ser usada como objeto de estudo para mim e para a comunidade e como referência para outros projetos. Por esses motivos, esse projeto sempre estará em constante adaptação, com adições de tecnologias e padrões que eu achar válidos para um desenvolvedor da área. Sintam-se livres para enviar sugestões e comentários, o debate é o mais importante.

O objetivo principal foi criar um sistema eficiente e seguro, com foco em alta performance e facilidade de manutenção, utilizando conceitos RESTful e tecnologias que nos permitam desenvolver uma aplicação robusta e escalável, tais como FastAPI, Docker e PostgreSQL.

## 2. Descrição técnica

### 2.1. Tecnologias utilizadas:
- **Python**: Linguagem principal de desenvolvimento, escolhida pela sua simplicidade e poder.
- **FastAPI**: Framework para construção de APIs com alta performance e suporte a tipagem assíncrona.
- **Docker**: Containerização para garantir a portabilidade e consistência do ambiente de desenvolvimento e produção.
- **PostgreSQL**: Banco de dados relacional robusto e escalável.
- **SQLAlchemy**: ORM para mapeamento objeto-relacional, facilitando a manipulação de dados.
- **Alembic**: Ferramenta para migração de banco de dados, garantindo a integridade e evolução do schema.

### 2.2. Principais funcionalidades da API:
- **CRUD Completo**: Operações de criação, leitura, atualização e exclusão de dados.
- **Autenticação JWT**: Implementação de autenticação segura para proteger os endpoints.
- **Documentação Automática**: Utilização do OpenAPI para geração automática da documentação da API.
- **Validação de Dados**: Validação rigorosa de entradas utilizando Pydantic.
- **Migrações de Banco de Dados**: Gerenciamento de mudanças no schema do banco de dados de forma segura com Alembic.

## 3. Destaques do Desenvolvimento:
- **Desempenho**: Adoção de práticas para garantir alta performance, como consultas otimizadas e uso de caching.
- **Escalabilidade**: Arquitetura projetada para escalar horizontalmente com facilidade.
- **Segurança**: Implementação de padrões de segurança, incluindo sanitização de inputs e prevenção contra ataques comuns como SQL Injection e XSS.
- **Testes Automatizados**: Cobertura abrangente com testes unitários e de integração para garantir a confiabilidade do sistema.
- **Monitoramento e Logging**: Integração com ferramentas de monitoramento e logging para rastreamento e diagnóstico em tempo real.

Este projeto demonstrou a importância de utilizar tecnologias modernas e práticas de desenvolvimento ágil para entregar uma solução de alta qualidade, pronta para suportar grandes volumes de dados e acessos simultâneos.

## 4. Estrutura de pastas e arquivos
```
.vscode/
    └── Instruções para o vscode deletar automaticamente arquivos e pastas "pycache"
apicultura/
    ├── core/
    │   ├── middlewares/
    │   ├── models/
    │   ├── schemas/
    │   ├── security/
    │   ├── database.py
    │   ├── dependencies.py
    │   ├── exceptions.py
    │   └── settings.py
    ├── migrations/
    │   ├── versions/
    │   └── env.py
    ├── tests/
    │   ├── factories/
    │   ├── v1/
    │   ├── conftest.py
    │   ├── test_app.py
    │   └── test_security.py
    ├── v1/
    │   ├── endpoints/
    │   ├── repo/
    │   ├── services/
    │   └── main.py
    └── main.py
htmlcov/
    └── Cobertura de código nos testes. Gerado pelo coverage
alembic.ini
docker-compose.yaml
Makefile
poetry.lock
pyproject.toml
```

## 5. CLI do projeto

### 5.1. Pré-requisitos:
1. Git
2. GNU Make
3. Docker e plugin Docker Compose

### 5.2. Instalação

Copie o repositório:
```bash
git clone https://github.com/asolheiro/APIcultura/
```

Instale as dependências:
```bash
make setup
make update
make dependencies
```

### 5.3. Rodando o banco de dados

Suba o banco de dados com o Docker Compose:
```bash
make db
```

Encerre a execução do banco de dados:
```bash
make db-stop
```

### 5.4. Rodando os servidores de desenvolvimento

Pode rodar tanto o servidor de desenvolvimento do próprio FastAPI:
```bash
make db
make run
```

Ou rodar o servidor usando o uvicorn, explicitando a porta:
```bash
make db
make run-api PORT={PORT}
```

### 5.5. Rodando os testes

Pode rodar apenas os testes:
```bash
make db
make unit
```

Ou então rodar os testes com a verificação de lint do Ruff:
```bash
make db
make test
```

### 5.6. Conteinerização

Construa as docker images da aplicação:
```bash
make build USER={USER}
```

Rode a aplicação a partir da imagem de container:
```bash
make db
make run-container USER={USER}
```

### 5.7. Migrações

Gere automaticamente o script de migrações do banco de dados:
```bash
make revision M={MESSAGE}
```

Aplique as migrações previamente geradas e corrigidas:
```bash
make migrate
```

> Para mais detalhes sobre o que cada comando "make" faz, dê uma olhada no arquivo [Makefile](Makefile)

## 6. Conclusão

Espero que este projeto sirva como uma base sólida para o estudo e compreensão das tecnologias envolvidas. Sinta-se à vontade para explorar, modificar e expandir o **APIcultura** conforme seu interesse e curiosidade.

Obrigado por ler e aproveitar o projeto!

> Caso precise de mais alguma informação ou ajuste, estou à disposição no e-mail: avgsolheiro@gmail.com!
