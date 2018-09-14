from config import *

yoNuncaKeyboard = types.InlineKeyboardMarkup()
yoNuncaKeyboard.add(types.InlineKeyboardButton('Me apunto', callback_data='yo'))

propuestaInlineKeyboard = types.InlineKeyboardMarkup()
propuestaInlineKeyboard.add(types.InlineKeyboardButton('Me apunto', callback_data='inlineApuntado'))


@bot.callback_query_handler(func=lambda call: call.data.startswith('propuesta'))
def function_button(call):
  
  mensaje = call.data.split(None, 1)[1]

  idUsuario = call.from_user.id
  nombreUsuario = call.from_user.username
  nombreUsuario = "@"+nombreUsuario
  
  todoCall = call
  print(str(todoCall))
  
 
  mid = call.inline_message_id
  
  
  contenido = mensaje + "\n\n"
  
  apuntados = mensaje.split("\n\n")[1:]
  
  #bot.answer_callback_query(call.id , str(mensaje) , show_alert=True)
  
  if nombreUsuario not in mensaje:
  
    mensaje = contenido  + nombreUsuario
     
    bot.answer_callback_query(call.id , "Vamos a apuntarte, apuntados: " + str(apuntados)  , show_alert=True)
    bot.edit_message_text(mensaje,  inline_message_id=call.inline_message_id , reply_markup=propuestaInlineKeyboard, parse_mode="Markdown")
    
    
    apuntados = mensaje.split("\n\n")[1:]
  
  
  else :

    apuntadosS = ""

    apuntados = mensaje.split("\n\n")[1:]

    contenido = mensaje.split("\n\n")[0]

    contenido = contenido + "\n\n"

    apuntados.remove(str(nombreUsuario))
  
    
    bot.answer_callback_query(call.id , str(apuntados) , show_alert=True)
                      

@bot.callback_query_handler(func=lambda call: call.data in ['yo'])
def callback_handlerYoNunca(call):
  
  cid = call.message.chat.id
  idUsuario = call.from_user.id
  
  if (call.from_user.username is None):
    bot.answer_callback_query(call.id, "Tienes que tener nickname, @ lo que sea", show_alert=True)
  else:
    nombreUsuario = call.from_user.username
    nombreUsuario = "@"+nombreUsuario

    mid = call.message.message_id
    mensaje = call.message.text

    contenido = mensaje + "\n\n"

    apuntados = mensaje.split("\n\n")[1:]


    if nombreUsuario == "@elraro":

      #print(str(call.id) + " " + nombreUsuario)
      bot.answer_callback_query(call.id, "HDP", show_alert=True)

    else:

      if nombreUsuario not in mensaje:

        mensaje = contenido  + nombreUsuario
        bot.edit_message_text(mensaje, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

        apuntados = mensaje.split("\n\n")[1:]
      else :

        apuntadosS = ""

        apuntados = mensaje.split("\n\n")[1:]

        contenido = mensaje.split("\n\n")[0]

        contenido = contenido + "\n\n"

        apuntados.remove(str(nombreUsuario))

        if len(apuntados) == 0 :

          bot.edit_message_text(contenido, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

        elif len(apuntados) == 1 :
            mensaje = contenido  + apuntados[0]
            bot.edit_message_text(mensaje, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

        elif len(apuntados) >= 1 : 
          for apuntado in apuntados:
            apuntadosS = apuntadosS + apuntado + "\n\n" 

          mensaje = contenido  + apuntadosS
          bot.edit_message_text(mensaje, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")
          

@bot.message_handler(func=lambda message: True)		# Respuestas del bot
def echo_message(message):
  cid = message.chat.id 				# Guardamos en la variale cid el id de el mensaje recibido 
  idUsu = message.from_user.id
  
  if message.text.lower().startswith("propuesta") and len(message.text)>1:
      cid = message.chat.id
      nombre = message.from_user.first_name
      mensaje = message.text
      
      respuesta = ' '.join(mensaje.split(" ")[1:])

      bot.send_message(cid, respuesta, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")