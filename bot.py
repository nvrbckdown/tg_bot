import telebot
import settings
import Keyboard
import bot_engine
from services import exchanges

bot = telebot.TeleBot(settings.TOKEN)

exchange = exchanges.Exchange()


def currency_checker(message):
    if message.text:
        return message.text.startswith('💵💴')
    else:
        return False


def currency_calculator_checker(message):
    if message.text:
        return message.text.startswith('💰')
    else:
        return False


def back_button_checker(message):
    if message.text:
        return message.text.startswith('↩')
    else:
        return False


@bot.message_handler(commands=['start'])
def start_command_handler(message):
    """Start command to start bot"""
    chat_id = message.chat.id
    bot.send_message(chat_id, "hello world", reply_markup=Keyboard.main_menu_keyboard())


@bot.message_handler(func=currency_checker)
def get_currency_handler(message):
    """Get currency rate from service and send it to user"""
    chat_id = message.chat.id
    currency_list = exchange.return_exchange_rate()
    msg = bot_engine.parse_coming_data(currency_list)
    bot.send_message(chat_id, msg, reply_markup=Keyboard.currency_markup())


@bot.message_handler(func=currency_calculator_checker)
def currency_calculator_handler(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Select⬇️", reply_markup=Keyboard.currency_select_markup())
    bot.register_next_step_handler(msg, select_convertion_type)


def select_convertion_type(message):
    if message.text == "🇺🇿 UZS to 💸":
        print("YES!")
    else:
        calculate(message)


def calculate(message):
    chat_id = message.chat.id
    text = message.text
    currency = text.split(" ")
    exchange.type_of_currency = currency[1]
    msg = bot.send_message(chat_id, "How much?")
    bot.register_next_step_handler(msg, return_calculation)


def return_calculation(message):
    amount = message.text
    try:
        amount_of_money = int(amount)
        if isinstance(amount_of_money, int):
            returning_value = exchange.return_calculation(amount_of_money)
            text_msg = bot_engine.get_country_flag(exchange.type_of_currency) + "{amount} {code} = 🇺🇿{rtn_value} UZS" \
                .format(amount=amount_of_money, code=exchange.type_of_currency, rtn_value=returning_value)
            bot.send_message(message.chat.id, text_msg, reply_markup=Keyboard.main_menu_keyboard())
    except Exception as e:
        msg = bot.send_message(message.chat.id, "You should write how much to convert!", parse_mode='Markdown')
        bot.register_next_step_handler(msg, return_calculation)


@bot.message_handler(func=back_button_checker)
def back_button_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Main menu⬇", reply_markup=Keyboard.main_menu_keyboard())


if __name__ == "__main__":
    bot.polling(none_stop=True)
