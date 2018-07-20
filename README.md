# Bot basico de ejemplo para Telegram, hecho en Python3 para mostrar ejemplos de funciones varias.

## Esto es posible gracias a https://github.com/sanguchi que creó toda la estructura del proyecto y siguiente tutorial de como utilizarlo:
## http://telegra.ph/Creando-Bots-en-Telegram-06-09

## Documentación para crear las funciones de bot.py:
>https://core.telegram.org/bots/api

## Primera clase 19/07/2018 Explicación de como utilizar glitch, bot reply y bot send message:
  
  ### Ejemplo creación de un comando
  >@bot.message_handler(commands=['start'])
  >def nombreComando(message):
    >bot.reply_to(message, 'Has iniciado el bot')
    
  ### Ejemplo respuestas bot
  >@bot.message_handler(func=lambda message: True)
  >def echo_message(message):
    >cid = message.chat.id
    
    if message.text.lower() == "hola":
      bot.send_message( cid, 'hola amigo')
  
