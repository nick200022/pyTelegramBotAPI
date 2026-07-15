import telebot


bot = telebot.TeleBot('8912482991:AAFwrMLTrKCichkG49okviuwX0JQD1G4AXY')

@bot.chat_join_request_handler(https://t.me/pcamacho1)
def make_some(message: telebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

bot.infinity_polling(allowed_updates=telebot.util.update_types)
if message.chat.type == "private":
    # private chat message

if message.chat.type == "group":
	# group chat message

if message.chat.type == "supergroup":
	# supergroup chat message

if message.chat.type == "channel":
	# channel message
