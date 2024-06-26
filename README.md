# Backend - Eco da Mata

## Como rodar o servidor

O Django é um servidor escrito em Python. Como ainda estamos trabalhando com ambientes virtuais, e não Docker, é necessário que você tenha o Python instalado em sua máquina e adicionado ao PATH. Recomendamos o Python 3.10.

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/Eco-da-Mata/mobileUEFS.git
    ```

2. **Caminhe para o diretório `backend/`:**
    ```bash
    cd eco-da-mata/backend/
    ```

3. **Utilize os comandos do Makefile para:**
    - **Criar o ambiente virtual:**
        ```bash
        make create-venv
        ```
    - **Ativar o ambiente virtual:**
        ```bash
        source venv/bin/activate
        ```
    - **Configurar o ambiente de desenvolvimento:**
        ```bash
        make setup
        ```
    - **Gerar uma nova SECRET_KEY e adicionar ao arquivo `.env`:**
        ```bash
        make generate-secret-key
        ```
    - **Instalar as dependências:**
        ```bash
        make install-deps
        ```
    - **Aplicar as migrações:**
        ```bash
        make migrate
        ```
    - **Executar o servidor de desenvolvimento do Django:**
        ```bash
        make runserver
        ```

Se você já estiver no ambiente virtual, basta executar `make setup` para instalar dependências, gerar nova chave secreta e realizar as migrações.

### Exemplo Sequencial

```bash
git clone https://github.com/Eco-da-Mata/mobileUEFS.git
cd eco-da-mata/backend/
make create-venv
source venv/bin/activate
make setup
make runserver
```

Obs: depois dessas configurações iniciais, não é mais necessário rodar o setup, apenas o runserver.

## Rotas disponíveis

- `127.0.0.1:8000/api/` - rota raíz. Apresenta todas as outras rotas de acesso da API.
- `127.0.0.1:8000/admin/` - painel administrativo. Permite que você faça uso de formulários para salvar dados no banco de dados.
- `127.0.0.1:8000/swagger/` - interface de documentação no formato Swagger.
- `127.0.0.1:8000/redoc/` - interface de documentação no formato ReDoc.

A porta padrão do Django é `8000`. Se quiser alterar, basta rodar:

```bash
python manage.py runserver ip:porta
```

Para acessar a plataforma admin, você precisa ter um superusuário. Para isso, basta rodar dentro do diretório backend/:

```bash
python manage.py createsuperuser
```

Informe os dados solicitados e você poderá acessar a plataforma admin.

## Escolhas no ambiente de desenvolvimento

- O banco de dados utilizado é o `db.sqlite3`, que permite o CRUD dentro do próprio servidor web. Escolhido pela facilidade de implementação. Para alterar, basta acessar o arquivo `backend/eco_da_mata/settings.py` e modificar a constante `DATABASES`.
- O servidor está com paginação implementada de 5 itens por página. Para alterar, basta acessar o arquivo `backend/eco_da_mata/settings.py` e modificar o valor em `REST_FRAMEWORK['PAGE_SIZE']`.
- As APIs só oferecem rotas do tipo GET, pois o CRUD completo acontecerá na plataforma admin.

## Escolhas no ambiente de produção (ainda não feito)

- Uso do banco de dados PostgreSQL.
- Uso do storage Supabase.
- Uso de Docker para criação de ambiente.
- Uso do Gunicorn (servidor WSGI (Web Server Gateway Interface) para aplicações web em Python).

## Utilitários

- No VSCode, você pode baixar o SQLite3 Editor para acessar e manipular dados diretamente do banco de dados.

