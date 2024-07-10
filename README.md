# Desenvolvimento de API RESTful com FastAPI, Docker, e PostgreSQL

## Sumário

1. [Descrição do projeto](#descrição-do-projeto)

2. [Descrição técnica](#descrição-técnica)

    2.1 [Tecnologias utilizadas](#tecnologias-utilizadas)
    
    2.2 [Principais funcionalidades da API](#principais-funcionalidades-da-api)

3. [Destaques do desenvolvimento](#destaques-do-desenvolvimento)

4. [Estrutura de pastas](#estrutura-de-pastas)

5. [Como rodar o projeto](#como-rodar-o-projeto)

    5.1 [Instalação](#instalação)

    5.2 [Rodando banco de dados](#rodando-banco-de-dados)

    5.3 [Rodando o servidor de desenvolvimento](#rodando_o-servidor-de-desenvolvimento)
    
    5.4 [Testes](#testes)

    5.4 [Conteinerização](#conteinerização)

    5.5 [Migrações](#migrações)

6. [Conclusão](#conclusão)


## Descrição do projeto

Esta é uma API genérica, criada com basa em um "ToDo Manager", um gerenciador de tarefas, mas feita para ser usada como objeto de estudo para mim e para a comunidade e como referência para outros projetos. Por estes motivos, esse projeto sempre estará em constante adaptação, com adições de tecnologias e padrões que eu achar válido para um desenvolvedor da área. Sintam-se livres para enviar sugestões e comentários, o debate é o mais importante.

Neste projeto, temos uma API RESTful robusta e escalável utilizando FastAPI, Docker e PostgreSQL. 
O objetivo principal é criar um sistema eficiente e seguro, com foco em alta performance e facilidade de manutenção. 


## Descrição técnica:

### **Tecnologias utilizadas:**
- **Python**: Linguagem principal de desenvolvimento, escolhida pela sua simplicidade e poder.
- **FastAPI**: Framework para construção de APIs com alta performance e suporte a tipagem assíncrona.
- **Docker**: Containerização para garantir a portabilidade e consistência do ambiente de desenvolvimento e produção.
- **PostgreSQL**: Banco de dados relacional robusto e escalável.
- **SQLAlchemy**: ORM para mapeamento objeto-relacional, facilitando a manipulação de dados.
- **Alembic**: Ferramenta para migração de banco de dados, garantindo a integridade e evolução do schema.

### **Principais funcionalidades da API:**
- **CRUD Completo**: Operações de criação, leitura, atualização e exclusão de dados.
- **Autenticação JWT**: Implementação de autenticação segura para proteger os endpoints.
- **Documentação Automática**: Utilização do OpenAPI para geração automática da documentação da API.
- **Validação de Dados**: Validação rigorosa de entradas utilizando Pydantic.
- **Migrações de Banco de Dados**: Gerenciamento de mudanças no schema do banco de dados de forma segura com Alembic.

## **Destaques do Desenvolvimento:**
- **Desempenho**: Adoção de práticas para garantir alta performance, como consultas otimizadas e uso de caching.
- **Escalabilidade**: Arquitetura projetada para escalar horizontalmente com facilidade.
- **Segurança**: Implementação de padrões de segurança, incluindo sanitização de inputs e prevenção contra ataques comuns como SQL Injection e XSS.
- **Testes Automatizados**: Cobertura abrangente com testes unitários e de integração para garantir a confiabilidade do sistema.
- **Monitoramento e Logging**: Integração com ferramentas de monitoramento e logging para rastreamento e diagnóstico em tempo real.

Este projeto demonstrou a importância de utilizar tecnologias modernas e práticas de desenvolvimento ágil para entregar uma solução de alta qualidade, pronta para suportar grandes volumes de dados e acessos simultâneos.


## Estrutura de pastas e arquivos
- **.vscode:** Instruções para o vscode deletar automaticamente arquivos e pastas "pycache'
- **apicultura/:** Pasta principal do projeto
   - **core/:** Diretório contendo funcionalidades a arquivos que não devem variar de versão para versão
        - **middlewares/:** Diretório para configuração dos middlewares pelo FastAPI
        - **models/:** Diretório de modelos para geração de tabelas no BD pelo sqlalchemy
        - **schemas/:** Schemas do Pydantic para validação dos dados
        - **security/:** Arquivos que realizam operações relacionadas à segurança da aplicação
        - */database.py:* Cria a engine e a sessão do BD
        - */dependencies.py:* Gerador de coneção do BD
        - */exceptions.py:* Tratamento personalizado de exceções da aplicação
        - */settings.py:* Leitor de variáveis de ambiente da aplicação
   - **migrations/:** Diretório de migrações do BD, gerado automaticamente pelos comandos do alembic
        - **versions/:** Diretório onde encontramos o versionamento de cada migração aplicada ao BD
        - */env.py:* Configurações de migrações do alembic
    - **tests/:** Diretório total de testes realizados pelo pytest
        - **factories/:** Diretório de definição das Factories usadas para gerar daddos nos testes
        - **v1/:** Testes unitários para operações e erros dos endpoints da v1
        - */conftest.py:* Definição da configurações das fixtures utilizadas nos testes
        - */test_app.py:* Teste da função root da aplicação
        - */test_security.py:* Teste das funcionalidades de segurança da aplicação
    - **v1/:** Diretório das funcionalidades da versão 1
        - **endpoints/:** Mapeamento dos endpoints da aplicação
        - **repo/:** Diretório principal de operações no banco de dados
        - **services/:** Diretório que define a lógica das operações da aplicação
        - */main.py:* Arquivo que monta as rotas da aplicação v1 e define a função root
    - */main.py:* Arquivo que monta as rotas da aplicação no geral
- **htmlcov/:** Cobertura de código nos testes. Gerado pelo coverage
- *alembic.ini:* Arquivo de inicialização do alembic, gerado automaticamente
- *docker-compose.yaml:* Arquivo para orquestração dos containers da aplicação e dos testes
- *Makefile:* Gerenciador de tasks do projeto
- *poetry.lock:* Gerenciador de dependências do Poetry
- *pyproject.toml:* Gerenciador do projeto.



## CLI do projeto
### Pré-requisitos:
1. (Git)[]

2. (GNU Make)[]

3. (Docker e plugin Docker Compose)[]


### Instalação

Copie o repositório
```bash
git clone https://github.com/rmndvngrpslhr/APIcultura/
```

Instale as dependências
```bash
make setup
make update
make dependencies
```

### Rodando o banco de dados
Suba o banco de dados com o Docker Compose:
```bash
make db
```

Encerre a execução do banco de dados:
```bash
make db-stop
```

### Rodando os servidores de desenvolvimento:
Pode rodar tanto o servidor de desenvolvimento do próprio FastAPI
```bash
make db
make run
```

Quanto rodar o servidor usando o uvicorn, explicitando a porta
```bash
make db
make run-api PORT={PORT}
```


### Rodando os testes:
Pode rodar apenas os testes
```bash
make db
make unit
```

Ou então rodar os testes com a verificação de lint do Ruff
```bash
make db
make test
```


### Conteinerização:
Construa as docker images da aplicação
```bash
make build USER={USER}
```

Rode a aplicação a partir da imagem de container
```bash
make db
make run-container USER={USER}
```


### Migrações
Gere automaticamente o script de migrações do banco de dados
```bash
make revision M={MESSAGE}
```

Aplique as migrações previamente geradas e corrigidas
```bash
make migrate
```

> Para mais detalhes sobre o que cada comando "make" faz, dê uma olhada no arquivo [Makefile](Makefile)


## Conclusão

Espero que este projeto sirva como uma base sólida para o estudo e compreensão das tecnologias envolvidas. Sinta-se à vontade para explorar, modificar e expandir o Travel Tracker conforme seu interesse e curiosidade.

Obrigado por ler e aproveitar o projeto!

> Caso precise de mais alguma informação ou ajuste, estou à disposição no e-mail: avgsolheiro@gmail.com!