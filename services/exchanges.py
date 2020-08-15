import requests
import json


class Exchange:
    """Exchange rate from NBU"""
    type_of_currency = ""
    amount_money = ""
    data_from_service = {}

    def __init__(self, type_of_currency="USD", amount=1):
        self.type_of_currency = type_of_currency
        self.amount_money = amount

    def __get_exchange_rates(self):
        # Get exchange rate json object from server
        req = requests.get("https://nbu.uz/en/exchange-rates/json/")
        self.data_from_service = req.json()
        return self.__get_data()

    def __get_data(self):
        convert_data = json.loads(json.dumps(self.data_from_service))
        sending_data = []
        for i in convert_data:
            if i["code"] in ["USD", "EUR", "RUB", "KZT", "GBP", "CHF"]:
                array_of_currency = [i["title"], i["code"], i["cb_price"]]
                sending_data.append(array_of_currency)
        return sending_data

    def __get_exact_data(self):
        """TODO parse data"""
        for i in self.data_from_service:
            get_data = json.loads(json.dumps(i))
            if self.type_of_currency == get_data["code"]:
                return get_data

    def __conversion_calculator(self):
        """TODO first get type of currency, than get second type to calculate"""
        self.__get_exchange_rates()
        print(self.type_of_currency)
        cb_price = self.__get_exact_data()
        return float(cb_price["cb_price"]) * self.amount_money

    def __reverse_convertion(self):
        self.__get_exchange_rates()
        cb_price = self.__get_exact_data()
        return self.amount_money / float(cb_price["cb_price"])

    def return_exchange_rate(self):
        # Return exchange rate as json
        return self.__get_exchange_rates()

    def return_calculation(self, amount):
        # return result of calculation
        self.amount_money = amount
        return str(round(self.__conversion_calculator()))

    def return_reverse_conversion(self):
        return str(round(self.__reverse_convertion()))


# if __name__ == "__main__":
#     exchange = Exchange(type_of_currency="EUR", amount=1)
#     exchange_rate = exchange.return_exchange_rate()
#     print(exchange_rate)
#     print("{amount} euro = {calculated} sum".format(amount=1, calculated=exchange.return_calculation(1)))