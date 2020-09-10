import requests
import json

class SearchCriteria:
    def __init__(self, accessToken):
        self.__accessToken= "Bearer "+accessToken
        self.__url = "https://plus.dnb.com/v1/search/criteria"
        self.__headers = {'Authorization':self.__accessToken, 'Content-Type': "application/json"}
        
    def getDunsNumber(self, searchTerm, countryCode):
        payload = "{ \"searchTerm\" : \""+searchTerm+"\" ,\"countryISOAlpha2Code\" : \""+countryCode+"\"}"
        response = requests.request("POST", self.__url, data = payload, headers = self.__headers)
        json_data = response.text
        dict_data = json.loads(json_data)
        duns_number=[]
        for i in range(0,dict_data["candidatesReturnedQuantity"]):
            duns_number.append(dict_data["searchCandidates"][i]["organization"]["duns"])
        return duns_number