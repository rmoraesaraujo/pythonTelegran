import os
from telethon import TelegramClient, events

# Lê as credenciais das variáveis de ambiente
api_id = os.getenv('API_ID')  # Defina a variável de ambiente API_ID
api_hash = os.getenv('API_HASH')  # Defina a variável de ambiente API_HASH
bot_token = os.getenv('BOT_TOKEN')  # Defina a variável de ambiente BOT_TOKEN

# Inicializa o cliente do Telethon com o bot token
client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

# Evento para monitorar mensagens em um canal
@client.on(events.NewMessage(chats='bigger_servidor'))
async def handler(event):
    keywords = ['꧁ঔৣ☬✞ 𝙄𝙉𝙁𝙊. 𝘽𝙇𝘼𝘿𝙀', '꧁ঔৣ☬✞ 𝙄𝙉𝙁𝙊. 𝘾𝙇𝙐𝘽 - 𝙄𝙋𝙏𝙑']
    destination_chat_id = 'rbplay27'  # Pode ser um chat privado ou outro canal/grupo
    if any(keyword.lower() in event.raw_text.lower() for keyword in keywords):
        print("Palavra-chave encontrada! Enviando a mensagem...")
        await client.send_message(destination_chat_id, event.message)

# Executa o cliente
with client:
    client.run_until_disconnected()
