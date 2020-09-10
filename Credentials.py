import requests
import json

class Credentials:
    def __init__(self):
        self.__url = "https://plus.dnb.com/v2/token"
        self.__payload = "{\"grant_type\" : \"client_credentials\"}"
        self.__headers = {'Content-Type': "application/json", 'Authorization':"Basic <<Base64 encoded String>>",'grant_type':"client_credentials"}
    def getAccessToken(self):
        response = requests.request("POST", self.__url, data=self.__payload, headers=self.__headers)
        json_data = json.loads(response.text)
        accessToken=json_data["access_token"]
        print("Access Token Received")
        return accessToken