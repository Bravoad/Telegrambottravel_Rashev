from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['history'])
def history(message: Message):
    bot.reply_to(message, "Команда в разработке")
