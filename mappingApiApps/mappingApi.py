import requests
import json

class ZipFetch:
    def __init__(self, apikey :str):
        self._headers :dict = {
            "apikey": apikey
        }

    def getZipResponse(self, url :str, params :tuple) -> list[int]:
        response = requests.get(url, headers=self._headers, params=params)
        responseJson = json.loads(response.text)
        response.close()

        if "error" in responseJson.keys():
            return []

        return responseJson["results"]

    def getZipByCity(self, city :str, countryCode :str, stateName :"optionalStr" = "") -> list[int]:
        url :str = "https://app.zipcodebase.com/api/v1/code/city"

        if(stateName):
            params = (
                ("city", city),
                ("state_name", stateName),
                ("country", countryCode)
            )
        else:
            params = (
                ("city", city),
                ("country", countryCode)
            )

        return self.getZipResponse(url, params)
    
    def getZipByRadius(self, originZipCode :str, radius :str, countryCode :str) -> list[int]:
        url :str = "https://app.zipcodebase.com/api/v1/radius"

        params = (
            ("code", originZipCode),
            ("radius", radius),
            ("country", countryCode),
            ("unit", "miles")
        )

        return self.getZipResponse(url, params)