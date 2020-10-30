import requests
import settings


class DictionaryService:
    """Word definition service which gets definition from an API based on word which is given by user"""

    def_of_word = ""

    def __init__(self, word):
        self.def_of_word = word

    def __get_definition(self):
        """Make get request to API to get data (definition)"""
        res = requests.get(settings.DIC_URL + self.def_of_word,
                           headers={'Authorization': 'token ' + settings.DIC_TOKEN})
        if res.status_code == 200:
            return res.json()
        else:
            return "Error"

    def get_meaning(self):
        """Return response as a service"""
        data = self.__get_definition()
        if data != "Error":
            response = {"def": data["definitions"][0]["definition"],
                        "example": data["definitions"][0]["example"],
                        "word": data['word']}
            return response
        else:
            return "Error"
