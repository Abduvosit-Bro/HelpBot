import telebot

bot = telebot.TeleBot("6107055262:AAGVxmYqkkOSDAKSp-t2zcliho5Cb12yr1w")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Напиши мне что-нибудь!")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Я повторяю за тобой все сообщения. Чтобы начать, нажми на /start")


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
