import requests
import json

url = "https://app.zipcodebase.com/api/v1/code/city"

params = (
    ("city", "San Francisco"),
    ("state_name","California"),
    ("country","us")
)

headers = {
    "apikey": "43ef42a0-75af-11ee-b46e-c76fdca57988"
}

response = requests.get(url, headers=headers, params=params)
responseJson = json.loads(response.text)
print(responseJson["results"])

class ZipFetch:
    def __init__(self, apikey :str):
        headers :dict = {
            "apikey": "43ef42a0-75af-11ee-b46e-c76fdca57988"
        }

    def getZipResponse(self, params :tuple) -> list[int]:
        response = requests.get(url, headers=headers, params=params)
        responseJson = json.loads(response.text)
        return responseJson["results"]

    def getZipByCity(self, city :str, state_name :"optionalStr", country :str) -> list[int]:
        if(state_name):
            params = (
                ("city", city),
                ("state_name", state_name),
                ("country", country)
            )
        else:
            params = (
                ("city", city),
                ("country", country)
            )

        return self.getZipResonse(params)

        