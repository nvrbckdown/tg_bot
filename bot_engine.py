from services import weather, dictionary
import datetime


def parse_coming_data(coming_data):
    msg = "📈Exchange rate by 🏦CB of Rep. of 🇺🇿Uzb \n\n"
    sorted_list = coming_data[::-1]
    for i in sorted_list:
        msg += get_country_flag(i[1]) + "1 {code} = {cb_price} sum".format(code=i[1], cb_price=i[2]) + "\n"
    return msg


def get_country_flag(code):
    if code == "USD":
        return "🇺🇸"
    elif code == "RUB":
        return "🇷🇺"
    elif code == "EUR":
        return "🇪🇺"
    elif code == "GBP":
        return "🇬🇧"
    elif code == "CHF":
        return "🇨🇭"
    elif code == "KZT":
        return "🇰🇿"
    else:
        return "hi"


def currency_checker(message):
    if message.text:
        return message.text.startswith('💵💴')
    else:
        return False


def feedback_checker(message):
    if message.text:
        return message.text.startswith('🖋')
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


def weather_checker(message):
    if message.text:
        return message.text.startswith('🌦')
    else:
        return False


def def_checker(message):
    if message.text:
        return message.text.startswith('📖')
    else:
        return False


def get_definition(word):
    def_word = dictionary.DictionaryService(word)
    coming_data = def_word.get_meaning()
    msg_text = "💬 Word: {word}\n"\
                "📇 Definition: {definition}\n"\
                "✏️ Example: {example}".format(word=coming_data['word'], definition=coming_data['def'],
                                               example=coming_data['example'])
    return msg_text


def get_weather_by_default():
    w = weather.Weather()
    weather_from_service = w.return_weather()
    msg_text = "***🏙 {city} \n\n🕔 {time} \n" \
               "🌡 Temperature: {temperature}°C\n" \
               "💧 Humidity: {humidity}\n" \
               "💨 Wind: {speed}m/s, {deg}°\n" \
               "🌎 Pressure: {press} P***".format(city=w.city, time=datetime.datetime.now(),
                                               temperature=weather_from_service[1]["temp"],
                                               humidity=weather_from_service[2], speed=weather_from_service[0]["speed"],
                                               deg=weather_from_service[0]["deg"], press=weather_from_service[3]["press"])
    return msg_text
