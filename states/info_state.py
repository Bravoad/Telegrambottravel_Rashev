from telebot.handler_backends import State, StatesGroup


class InfoState(StatesGroup):
    city = State()
    count = State()
    is_photo = State()
