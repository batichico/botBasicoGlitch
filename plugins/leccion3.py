from config import *

#Inicio charla 3 - 08/08/2018

@bot.message_handler(func=lambda message: True)		# Respuestas del bot
def echo_message(message):
  cid = message.chat.id 				# Guardamos en la variale cid el id de el mensaje recibido 
  idUsu = message.from_user.id
  
  
  if message.text.lower().startswith('participo con el numero'):

      cid = message.chat.id
      mensaje=message.text
      rnd = randrange(0, int(9))
      respuesta = ' '.join(mensaje.split(" ")[4:])

      #bot.send_message(cid, "la respuesta es: " + respuesta)
      #bot.send_message(cid, str(rnd))

      if int(respuesta) == rnd:
        bot.send_message(cid, "Has acertado")

      else:
        bot.send_message(cid, "Has fallado, el número era " + str(rnd))

  #Fin charla 3 - 08/08/2018