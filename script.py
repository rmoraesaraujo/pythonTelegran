from telethon import TelegramClient, events

# Insira suas credenciais do Telegram
api_id = '24446798'
api_hash = 'ee38eed42c07719909e35a96c096e3be'
phone = '+5511970640032'  # Opcional, necessário para a primeira autorização
keywords = ['꧁ঔৣ☬✞ 𝙄𝙉𝙁𝙊. 𝘽𝙇𝘼𝘿𝙀', '꧁ঔৣ☬✞ 𝙄𝙉𝙁𝙊. 𝘾𝙇𝙐𝘽 - 𝙄𝙋𝙏𝙑']
destination_chat_id = 'rbplay27'  # Pode ser um chat privado ou outro canal/grupo

# Inicializa o cliente
client = TelegramClient('session_name', api_id, api_hash)

# Evento para monitorar mensagens em um canal
@client.on(events.NewMessage(chats='bigger_servidor'))
async def handler(event):
    # Verifica se alguma das palavras-chave está presente no texto da mensagem
    if any(keyword.lower() in event.raw_text.lower() for keyword in keywords):
        print("Palavra-chave encontrada! Enviando a mensagem...")
        await client.send_message(destination_chat_id, event.message)

# Executa o cliente
with client:
    client.run_until_disconnected()