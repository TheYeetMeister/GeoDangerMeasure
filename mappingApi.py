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

def getZipByCity(city :str, state_name :"optionalStr", country :str) -> list[int]:
    