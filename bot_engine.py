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
