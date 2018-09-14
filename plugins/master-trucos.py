from config import *

@bot.message_handler(func=lambda message: True)		# Respuestas del bot
def echo_message(message):
  cid = message.chat.id 				# Guardamos en la variale cid el id de el mensaje recibido 
  idUsu = message.from_user.id
  
  if message.text.lower() ==  "bot vete" :
    
    if idUsu== 239822769:
      bot.send_message(cid, 'vale :C, adios mi gente!')	
      bot.leave_chat(cid)
      
  if len(set(message.text.lower().split()) & set(('martillazo','banea','baneiyo')))>0 :
      
    bot.send_message(cid, 'Martillazo rico')	