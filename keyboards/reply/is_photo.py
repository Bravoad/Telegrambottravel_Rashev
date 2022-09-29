from telebot.types import Message,ReplyKeyboardMarkup
from states.info_state import InfoState
from loader import bot


@bot.message_handler(state=InfoState.is_photo)
def show_or_not_to_show_hotels_photo(message: Message) -> None:
    """
    Данная функция спрашивает у пользователя: показать фото?
    :param message:
    :return:
    """

    photo_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    photo_markup.add("Да", "Нет")
    msg = bot.send_message(message.chat.id, "Показать фото?", reply_markup=photo_markup)
    bot.register_next_step_handler(msg)
