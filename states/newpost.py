from aiogram.dispatcher.filters.state import StatesGroup, State


class NewPost(StatesGroup):
    picture = State()
    video = State()
    document = State()
    text = State()

