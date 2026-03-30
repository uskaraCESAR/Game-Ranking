# Game Ranking

Projeto desenvolvido em Django para avaliacao de games e publicacao de criticas.

## Descricao

O objetivo do sistema e permitir que usuarios consultem, avaliem e compartilhem opinioes sobre jogos em uma plataforma simples e organizada.

## Tecnologias

- Python
- Django
- Selenium

## Como executar o projeto

1. Crie e ative um ambiente virtual.
2. Instale as dependencias:

```bash
pip install -r requirements.txt
```

3. Execute as migracoes:

```bash
python manage.py migrate
```

4. Inicie o servidor:

```bash
python manage.py runserver
```

## Deploy no Render com PostgreSQL

O projeto ja esta preparado para:

- usar `SQLite` localmente quando `DATABASE_URL` nao estiver definida
- usar `PostgreSQL` no Render quando `DATABASE_URL` estiver definida
- criar ou atualizar um superusuario automaticamente no deploy usando variaveis de ambiente

### Arquivos de deploy

- `build.sh`: instala dependencias, roda `collectstatic`, `migrate` e `ensure_superuser`
- `render.yaml`: define o banco PostgreSQL e o servico web no Render
- `accounts/management/commands/ensure_superuser.py`: cria ou atualiza o superusuario sem prompt interativo

### Variaveis de ambiente importantes

No Render, configure estas variaveis no servico web:

```text
SECRET_KEY=gere-uma-chave-segura
DEBUG=False
ALLOWED_HOSTS=seu-servico.onrender.com
CSRF_TRUSTED_ORIGINS=https://seu-servico.onrender.com
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@exemplo.com
DJANGO_SUPERUSER_PASSWORD=uma-senha-forte
```

Se estiver usando o `render.yaml`, o `DATABASE_URL` ja sera ligado automaticamente ao banco criado no Blueprint.

### Fluxo recomendado

1. Suba o projeto para o GitHub.
2. No Render, crie o deploy via `Blueprint` apontando para este repositorio.
3. Antes do primeiro deploy terminar, confira as variaveis de ambiente do servico.
4. No fim do deploy, o Render vai:
   - instalar dependencias
   - coletar os arquivos estaticos
   - aplicar migracoes
   - criar ou atualizar o superusuario
5. Acesse `/admin` com o usuario configurado nas variaveis `DJANGO_SUPERUSER_*`.

### Migrando dados do SQLite para PostgreSQL

Se voce quiser levar os dados atuais do `db.sqlite3` para o PostgreSQL:

```bash
python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.permission --indent 2 > data.json
```

Depois de apontar `DATABASE_URL` para o PostgreSQL e rodar `migrate`:

```bash
python manage.py loaddata data.json
```

Se preferir, voce tambem pode comecar com o banco novo vazio e deixar apenas o superusuario ser criado no primeiro deploy.

## Colaboradores

- Arthur de Almeida Oliveira
- Arthur Filipe Silva dos Reis
- Gabriel Gondim Malta
- Gabriel Mendes Cavalcanti
- Guilherme Silva Guimaraes
- Helio de Moraes Rego Neto
- Matheus Assis de Souza Jacome

## Entrega 01

- Figma: https://www.figma.com/board/fm0wB9xITXtjeqBeBZYJjj/Sem-t%C3%ADtulo?node-id=0-1&t=9dShIyt3maLOlE0m-1
- Historias do projeto: https://docs.google.com/document/d/1koSvhLiN-m2yipQsbQeLWTG0vbIIWovv3-FDx5r-KnA/edit?tab=t.0
- Prints do Jira: https://drive.google.com/drive/folders/187pxLEDKzr8ZbCQJDWKPiKosjQO6r-wn?usp=sharing
- Screencast: https://www.youtube.com/watch?v=V_xk95SDth4

## Entrega 02

- Prints do Jira: https://drive.google.com/drive/folders/187pxLEDKzr8ZbCQJDWKPiKosjQO6r-wn?usp=sharing
- Screencast: https://youtu.be/GMoFRywxXDE
- Relatório pair programing: https://docs.google.com/document/d/1ghc7w0ws937uktHESDruGyv4_7DGh1inWLtMlZLwBgc/edit?usp=sharing

## Observacoes

Como o repositório ainda nao possui a estrutura completa do Django versionada, os comandos acima assumem que o arquivo `manage.py` e o projeto Django serao adicionados ou ja existem no ambiente local de desenvolvimento.
