from config import *

#Inicio charla 4 - 29/08/2018

menuKeyboard = types.InlineKeyboardMarkup()
menuKeyboard.add(types.InlineKeyboardButton('Ayuda', callback_data='ayuda'),
           types.InlineKeyboardButton('Creador', callback_data='creador'))

@bot.message_handler(commands=['menu'])
def menu(m):

  cid = m.chat.id
  bot.send_message(cid, "Menu", reply_markup=menuKeyboard, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data in ['ayuda', 'creador'])
def callback_handlerMenu(call):
  
  cid = call.message.chat.id
  mid = call.message.message_id
  info = call.data
  
  #bot.send_message(cid, "Has pulsado " + str(info))
  
  if info == "ayuda":
    #bot.send_message(cid, "Entramos en  " + str(info))
    
    bot.edit_message_text("Has pulsado ayuda", cid, mid, reply_markup=menuKeyboard, parse_mode="Markdown")
    
  elif info == "creador":
    
    #bot.send_message(cid, "Entramos en  " + str(info))
    
    bot.edit_message_text("Mi creador es : @batichico" , cid, mid, reply_markup=menuKeyboard , parse_mode="Markdown")
        
  #Fin charla 4 - 29/08/2018