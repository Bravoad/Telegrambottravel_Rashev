from telebot.types import Message
from states.info_state import InfoState
from loader import bot
from keyboards.reply.is_photo import show_or_not_to_show_hotels_photo

@bot.message_handler(commands=['bestdeal'])
def bestdeal(message: Message):
    bot.set_state(message.from_user.id, InfoState.city, message.chat.id)
    bot.send_message(message.from_user.id, f"Привет {message.from_user.username} Введите город где нужно показать отели.")


@bot.message_handler(state=InfoState.city)
def get_city(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.from_user.id, "Записал, введите количество отображаемых отелей.")
        bot.set_state(message.from_user.id, InfoState.count, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['city'] = message.text
    else:
        bot.send_message(message.from_user.id, "Некорректный ввод, введите только буквы")


@bot.message_handler(state=InfoState.count)
def get_count(message: Message) -> None:
    if message.text.isdigit():
        bot.send_message(message.from_user.id, "Записал, вам нужно фото?",reply_markup=show_or_not_to_show_hotels_photo)
        bot.set_state(message.from_user.id, InfoState.is_photo, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['count'] = message.text
    else:
        bot.send_message(message.from_user.id, "Некорректный ввод, введите только цифры")
