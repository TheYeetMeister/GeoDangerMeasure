import requests
import json

class ZipFetch:
    def __init__(self, apikey :str):
        self._headers :dict = {
            "apikey": apikey
        }

    def getZipResponse(self, url :str, params :tuple) -> list[int]:
        '''gets response from api and closes the response'''
        response = requests.get(url, headers=self._headers, params=params)
        responseJson = json.loads(response.text)
        response.close()

        if "error" in responseJson.keys():
            return []

        return responseJson["results"]

    def getZipByCity(self, city :str, countryCode :str, stateName :"optionalStr" = "") -> list[int]:
        '''gets the zip code of a city with a given country, state name is optional'''
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
    
    def getZipByRadius(self, originZipCode :str, radius :str, countryCode :str) -> set[str]:
        '''fetches a list of zip codes from an origin zip code with a given radius in miles and
        country code'''
        url :str = "https://app.zipcodebase.com/api/v1/radius"

        params = (
            ("code", originZipCode),
            ("radius", radius),
            ("country", countryCode),
            ("unit", "miles")
        )

        '''little complex but the getZipResonse returns a list of dictionaries with all information including
        city name, state, etc. this lambda function iterates through the list of dictionaries
        and appends only the zip codes to this empty list'''
        return {data["city"] for data in self.getZipResponse(url, params)}