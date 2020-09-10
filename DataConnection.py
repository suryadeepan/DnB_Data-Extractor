import socket
import http.client

class DataConnection:
    def __init__(self, accessToken):
        self.__accessToken= "Bearer "+accessToken
        self.__conn = http.client.HTTPSConnection("plus.dnb.com")
        self.__headers = {'authorization':self.__accessToken, 'accept': "application/json"}
        
    def AASBIG(self, dunsnumber):
        url_string="https://plus.dnb.com/v1/data/duns/"+str(dunsnumber)+"?productId=aasbig&versionId=v1"
        self.__conn.request("GET", url_string, headers= self.__headers)
        return self.__conn.getresponse().read()
    def AASMCU(self, dunsnumber):
        url_string="https://plus.dnb.com/v1/data/duns/"+str(dunsnumber)+"?productId=aasmcu&versionId=v1"
        self.__conn.request("GET", url_string, headers= self.__headers)
        return self.__conn.getresponse().read()
    def AASDHQ(self, dunsnumber):
        url_string="https://plus.dnb.com/v1/data/duns/"+str(dunsnumber)+"?productId=aasdhq&versionId=v1"
        self.__conn.request("GET", url_string, headers= self.__headers)
        return self.__conn.getresponse().read()
    def LNKALT(self, dunsnumber):
        url_string="https://plus.dnb.com/v1/data/duns/"+str(dunsnumber)+"?productId=lnkalt&versionId=v1"
        self.__conn.request("GET", url_string, headers= self.__headers)
        return self.__conn.getresponse().read()
    def LNKMIN(self, dunsnumber):
        url_string="https://plus.dnb.com/v1/data/duns/"+str(dunsnumber)+"?productId=lnkmin&versionId=v1"
        self.__conn.request("GET", url_string, headers= self.__headers)
        return self.__conn.getresponse().read()
    def LNKUPD(self, dunsnumber):
        url_string="https://plus.dnb.com/v1/data/duns/"+str(dunsnumber)+"?productId=lnkupd&versionId=v1"
        self.__conn.request("GET", url_string, headers= self.__headers)
        return self.__conn.getresponse().read()
    def CMPELK(self, dunsnumber):
        url_string="https://plus.dnb.com/v1/data/duns/"+str(dunsnumber)+"?productId=cmpelk&versionId=v1"
        self.__conn.request("GET", url_string, headers= self.__headers)
        return self.__conn.getresponse().read()