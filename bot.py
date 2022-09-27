import telebot
bot = telebot.TeleBot('5334941052:AAE6aEYY1j-QkIdnN4DngZ9PRATi4s_faUI')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/lowprice":
        bot.send_message(message.from_user.id, "Команда в разработке")
    elif message.text == "/highprice":
        bot.send_message(message.from_user.id, "Команда в разработке")
    elif message.text == "/history":
        bot.send_message(message.from_user.id, "Команда в разработке")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Команда в разработке")
    elif message.text == "Пока":
        bot.send_message(message.from_user.id, "Пока")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
