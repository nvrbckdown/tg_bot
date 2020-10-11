import requests
import settings


class DictionaryService:

    def_of_word = ""

    def __init__(self, word):
        self.def_of_word = word

    def __get_definition(self):
        res = requests.get(settings.DIC_URL + self.def_of_word,
                           headers={'Authorization': 'token ' + settings.DIC_TOKEN}).json()
        return res

    def get_meaning(self):
        data = self.__get_definition()
        response = {"def": data["definitions"][0]["definition"],
                    "example": data["definitions"][0]["example"],
                    "word": data['word']}
        return response
