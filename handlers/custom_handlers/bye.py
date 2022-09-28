from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['bye'])
def bot_bye(message: Message) -> None:
    bot.reply_to(message, f"Пока, {message.from_user.full_name}!")
