import telebot

bot = telebot.TeleBot("8912482991:AAFwrMLTrKCichkG49okviuwX0JQD1G4AXY") # You can set parse_mode by default. HTML or MARKDOWN
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
  bot.infinity_polling(@bot.chat_join_request_handler(https://t.me/pcamacho1) # <- passes ChatInviteLink type object to your function)
@bot.message_handler(filters)
                  #import telebot
bot = telebot.TeleBot("8912482991:AAFwrMLTrKCichkG49okviuwX0JQD1G4AXY")

# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	pass

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	pass

# Handles all text messages that match the regular expression
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass

# Handles all messages for which the lambda returns True
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
	pass

# Which could also be defined as:
def test_message(message):
	return message.document.mime_type == 'text/plain'

@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
	pass

# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# This handler will be called if the message starts with '/hello' OR is some emoji
@bot.message_handler(commands=['hello'])
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
def send_something(message):
  
@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    # Query message is text
    pass)
def function_name(message):
	bot.reply_to(message, "This is a message handler")
  @bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

  @bot.callback_query_handler(func=lambda call: True)
def test_callback(call): # <- passes a CallbackQuery type object to your function
    logger.info(call)
