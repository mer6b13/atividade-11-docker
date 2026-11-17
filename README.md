# Atividade 11 — Docker

## Objetivo
Aprender o conceito de containerização e executar uma aplicação Python dentro de containers Docker.

## Tecnologias utilizadas
- Python 3.12
- Flask
- Docker
- Docker Compose
- PostgreSQL 16

## Estrutura do projeto
- app.py
- requirements.txt
- Dockerfile
- docker-compose.yml
- README.md

## Construir a imagem Docker

```bash
docker build -t atividade11-docker .
```

## Executar o container individualmente

```bash
docker run -d -p 5000:5000 --name atividade11-container atividade11-docker
```

## Executar com Docker Compose

```bash
docker compose up -d --build
```

## Verificar os containers

```bash
docker compose ps
```

## Consultar os logs

```bash
docker compose logs
```

## Acessar a API

http://127.0.0.1:5000/

## Listar produtos

http://127.0.0.1:5000/produtos

## Consultar configuração

http://127.0.0.1:5000/configuracao

## Parar os containers

```bash
docker compose down
```

## Desafio extra
Utilização do Docker Compose para executar a API Flask e o banco de dados PostgreSQL em containers separados.

## Objetivo
Executar uma API Python dentro de um container Docker.

## Tecnologias utilizadas
- Python
- Flask
- Docker

## Arquivos do projeto
- app.py
- requirements.txt
- Dockerfile

## Construir a imagem

docker build -t atividade11-docker .

## Executar o container

docker run -d -p 5000:5000 --name atividade11-container atividade11-docker

## Verificar o container

docker ps

## Acessar a API

http://127.0.0.1:5000/

## Listar produtos

http://127.0.0.1:5000/produtos

## Consultar configuração

http://127.0.0.1:5000/configuracao

## Consultar logs

docker logs atividade11-container

## Parar o container

docker stop atividade11-container