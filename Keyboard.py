from telebot import types


# Select language keyboard
def select_language():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    buttonUzbek = types.KeyboardButton("🇺🇿 O`zbek Tili")
    buttonRus = types.KeyboardButton("🇷🇺 Русский язык")
    markup.add(buttonUzbek, buttonRus)
    return markup


#Main menu keyboard
def main_menu_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn_get_exchanges = types.KeyboardButton("💵💴Exchange Rates💶💷")
    btn_get_weather = types.KeyboardButton("🌦 Weather")
    btn_get_def = types.KeyboardButton("📖 Get Definition")
    feed_back_btn = types.KeyboardButton("🖋Feedback")
    markup.add(btn_get_exchanges)
    markup.add(btn_get_weather)
    markup.add(btn_get_def)
    markup.add(feed_back_btn)
    return markup


def command_help_board():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    buttonRestart = types.KeyboardButton("🔄RESTART🔄")
    markup.add(buttonRestart)
    return markup


def currency_select_menu_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(types.KeyboardButton("🇺🇿 UZS to 💸"))
    markup.add(types.KeyboardButton("🇺🇸 USD"), types.KeyboardButton("🇷🇺 RUB"))
    markup.add(types.KeyboardButton("🇪🇺 EUR"), types.KeyboardButton("🇬🇧 GBP"))
    markup.add(types.KeyboardButton("🇨🇭 CHF"), types.KeyboardButton("🇰🇿 KZT"))
    return markup


def currency_select_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(types.KeyboardButton("🇺🇸 USD"), types.KeyboardButton("🇷🇺 RUB"))
    markup.add(types.KeyboardButton("🇪🇺 EUR"), types.KeyboardButton("🇬🇧 GBP"))
    markup.add(types.KeyboardButton("🇨🇭 CHF"), types.KeyboardButton("🇰🇿 KZT"))
    markup.add(types.KeyboardButton("↩️Back"))
    return markup


def currency_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn_get_exchanges = types.KeyboardButton("💰 Currency Calculator")
    btn_get_weather = types.KeyboardButton("↩️Back")
    markup.add(btn_get_exchanges, btn_get_weather)
    return markup