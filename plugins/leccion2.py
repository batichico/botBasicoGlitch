from config import *
#Inicio charla 2 - 31/07/2018

@bot.message_handler(commands=['ruleta'])
def ruleta(message):

  cid = message.chat.id
  nombreUsuario = message.from_user.username
  idUsuario = message.from_user.id
  rnd = randrange(0, int(5))

  if rnd == 4:
    bot.send_message(cid, "Pummmm tas muelto @" + nombreUsuario )
    bot.kick_chat_member(cid,idUsuario)
    bot.unban_chat_member(cid, idUsuario)

  else:

    bot.send_message(cid, "Te has salvado amijo @" + nombreUsuario)
    

@bot.message_handler(func=lambda message: True)		# Respuestas del bot
def echo_message(message):
  cid = message.chat.id 				# Guardamos en la variale cid el id de el mensaje recibido 
  idUsu = message.from_user.id
  
  if "boti di" in message.text.lower():               # Comparamos el texto el mensaje si es igual a "boti di"

      cid = message.chat.id                              #Id del chat
      mensaje=message.text                               #Mensaje completo
      respuesta = ' '.join(mensaje.split(" ")[2:])       #Respuesta
      bot.send_message(cid, respuesta)                   #El bot envía la respuesta


#Respuesta a la entrada de un usuario al grupo 
@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def command_bienvenida(m):
    cid = m.chat.id                                    #Id del chat
    cname = m.chat.title                               #Nombre del grupo
    bienvenida = ""                                    #Variable dónde guardaremos el mensaje de bienvenida

    infoMesaje = str(m)
    
    nuevoUsuarioId = m.new_chat_member.id
    nuevoUsuarioName = m.new_chat_member.username
    añadidoPorId = m.from_user.id
    añadidoPor = m.from_user.username
    
    #bot.send_message(cid, infoMesaje) 
    if nuevoUsuarioName == "Botinutilbot":
     
      if cid != -1001318959349:
        
        bot.send_message(cid, añadidoPor + " , para que hostias me metes, este no es mi grupo joderrr!")
        bot.leave_chat(cid)
      
      
    if añadidoPorId == nuevoUsuarioId:
      bot.send_message(cid, 'Entrado por enlace de invitación') 
      
      
      #bot.send_message(cid, infoMesaje) 
    else:
      bot.send_message(cid, 'añadido por: ' + añadidoPor) 
      bot.send_message(cid, str(cid)) 
      
    if (m.new_chat_member.username is None):           #Si el usuario no tiene nickname
        nun = m.new_chat_member.first_name             #Guardamos el primer nombre del usuario
        
        if (m.new_chat_member.last_name is not None):  #Si el usuario tiene apellido
            nun += " "                        
            nun += m.new_chat_member.last_name         #Se guarda el apellido
            
        else:                                          #Si no tiene apellido
            bienvenida = "Bienvenido al grupo"         #Se guarda "Bienvenido al grupo"
            bienvenida += str(cname)                   #Se le añade el nombre del chat detras de "Bienvenido al grupo"
            bienvenida += " "
    else:                                              #Si el usuario tiene nickname
        nun = m.new_chat_member.username               #Se guarda en nun el nickname del usuario
        bienvenida = "Bienvenido al grupo "            #Se guarda "Bienvenido al grupo"
        bienvenida += str(cname)                       #Se le añade el nombre del chat detras de "Bienvenido al grupo"
        bienvenida += " @"

    bot.send_message(cid, str(bienvenida) + str(nun))  #Se envía el mensaje de bienvenida concatenando el nombre/nickname del usuario

    
#Respuesta a la salida de un usuario del grupo 
@bot.message_handler(func=lambda message: True, content_types=['left_chat_member'])
def command_bye(m):
    cid = m.chat.id                                    #Id del grupo
    despedida = ""                                     #Variable dónde guardaremos el mensaje de despedida
    
    if (m.left_chat_member.username is None):          #Si el usuario no tiene nickname
        nun = m.left_chat_member.first_name            #Guardamos el primer nombre del usuario
        
        if (m.left_chat_member.last_name is not None): #Si el usuario tiene apellido
            nun += " "
            nun += m.left_chat_member.last_name        #Se guarda el apellido
            
    else:                                              #Si el usuario tiene nickname
        nun = m.left_chat_member.username              #Se guarda en nun el nickname del usuario
        despedida = "Hasta luego "                     #Se guarda "Hasta luego"
        despedida += " @"

    bot.send_message(cid, str(despedida) + str(nun))   #Se envía el mensaje de despedida concatenando el nombre/nickname del usuario

  