# Teste Djavue

## Descrição
Rota /dashboard possui 1 campo de busca, filtrando por nome de vendedor, cliente e data da venda. Apos a abordagem, tem o botao para "filtrar" que ira renderizar os dados das vendas existentes baseado em no campo de filtro, possui tambem 2 botoes para gerar os relatorios das vendas em pdf ou em excel.

## Pré-requisitos
- Python 3.11
- Node.js e npm
- Docker (opcional, se estiver usando Docker)

## Configuração do Ambiente de Desenvolvimento
1. Clone o repositório: `git clone `
2. Navegue até o diretório do projeto: `cd backend`
3. Instale as dependências do backend: `pip install -r requirements.txt`
4. Navegue até o diretório do frontend: `cd frontend`
5. Instale as dependências do frontend: `npm install`
6. Volte para o diretório raiz do projeto: `cd ..`

## Executando o Projeto
### Backend
1. Navegue até o diretório do backend: `cd backend`
2. Execute o servidor Django: `python manage.py runserver`

### Frontend
1. Navegue até o diretório do frontend: `cd frontend`
2. Inicie o servidor de desenvolvimento do Vue: `npm run serve`

## Configuração do Docker (opcional)
1. Certifique-se de que o Docker está instalado e em execução em sua máquina.
2. Na raiz do projeto, execute: `docker-compose up --build`
3. O projeto estará disponível em `http://localhost:8000/` (backend) e `http://localhost:8080/` (frontend).


