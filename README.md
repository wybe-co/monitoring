# Monitoramento de Containers

Este repositório foi criado no intuito de praticar o monitoramento de containers a partir de webhooks gerados pelo discord.

A ideia é um verificador de saúde de API's que retorna um json para cada verificação feita a cada 15 minutos e após a verificação retorna uma mensagem via discord com o status da API.

## O que foi usado?

- Github Actions - CI/CD
- Docker - Gerenciamento de Container
- API - Open source
- Python - Aplicação que realiza o monitoramento
  -  Requisitos utilizadas: Flask, requests, sqlalchemy e pytest

## Testar localmente

Caso queira testar o funcionamento da aplicação localmente basta buildar e rodar o container e acessar o endpoint http://localhost:5000/monitor

```
Comandos:

  docker build -t api-monitor .
  docker run -d --name api-monitor-container -p 5000:5000 api-monitor
```

### OBS: Interação com IA

- Código da aplicação gerado por IA, poder ocorrer erros e redundâncias. O intuito do projeto é o teste de workflows a partir do Github Actions.
