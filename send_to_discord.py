import json
import os
import requests

# Ler o arquivo results.json
with open("results.json", "r") as f:
    monitor_data = json.load(f)

# Verificar se é uma lista e converter para o formato esperado
if isinstance(monitor_data, list):
    embed_fields = [
        {
            "name": api["name"],
            "value": f"**Status:** {api['status']}\n**Tempo de Resposta:** {api.get('response_time', 'N/A')}s",
            "inline": True
        }
        for api in monitor_data
    ]
else:
    raise ValueError("Formato inesperado em results.json. Esperado uma lista.")

# Criar a mensagem no formato do Discord
discord_message = {
    "content": "🔍 **Resultados do monitoramento:**",
    "embeds": [
        {
            "title": "Detalhes do Monitoramento",
            "fields": embed_fields,
            "color": 65280 if all(api["status"] == 200 for api in monitor_data) else 16711680
        }
    ]
}

# Enviar ao Discord via Webhook
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
response = requests.post(webhook_url, json=discord_message)

# Verificar se o envio foi bem-sucedido
if response.status_code == 204:
    print("Mensagem enviada com sucesso!")
else:
    print(f"Erro ao enviar mensagem: {response.status_code}, {response.text}")