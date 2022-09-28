from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['lowprice'])
def lowprice(message: Message):
    bot.reply_to(message, "Команда в разработке")
