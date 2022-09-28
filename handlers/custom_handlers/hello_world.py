from telebot.types import Message
from states.contact_state import UserInfoState
from loader import bot


@bot.message_handler(commands=['hello_world'])
def hello_world(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.name, message.chat.id)
    bot.send_message(message.from_user.id, f"Привет {message.from_user.username} Введите имя.")


@bot.message_handler(state=UserInfoState.name)
def get_name(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.from_user.id, "Записал, введите свой возраст")
        bot.set_state(message.from_user.id, UserInfoState.age, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['name'] = message.text
    else:
        bot.send_message(message.from_user.id, "Некорректный ввод, введите только буквы")


@bot.message_handler(state=UserInfoState.age)
def get_age(message: Message) -> None:
    if message.text.isdigit():
        bot.send_message(message.from_user.id, "Записал, введите свой возраст")
        bot.set_state(message.from_user.id, UserInfoState.country, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['age'] = message.text
    else:
        bot.send_message(message.from_user.id, "Некорректный ввод, введите только цифры")


@bot.message_handler(state=UserInfoState.country)
def get_country(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.from_user.id, "Записал, введите свою страну ")
        bot.set_state(message.from_user.id, UserInfoState.city, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['country'] = message.text
    else:
        bot.send_message(message.from_user.id, "Некорректный ввод, введите только буквы")


@bot.message_handler(state=UserInfoState.country)
def get_city(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.from_user.id, "Записал, введите свой город ")
        bot.set_state(message.from_user.id, UserInfoState.phone_number, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['city'] = message.text
    else:
        bot.send_message(message.from_user.id, "Некорректный ввод, введите только буквы")
