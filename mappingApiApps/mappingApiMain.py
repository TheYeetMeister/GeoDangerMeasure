import mappingApi

def getRadiusZips() -> list[int]:
    apikey :str = input("What is your Apikey? :")
    originZip :str = input("What is the origin of your radius (please respond with a zip)? :")
    radius :str = input("What is the radius in which you want to collect zips? :")
    countryCode :str = input("What is the country code of the country where you want to collect zips? :")

    return mappingApi.ZipFetch(apikey).getZipByRadius(originZip, radius, countryCode)

def getCityZips() -> list[int]:
    apikey :str = input("What is your Apikey? :")
    city :str = input("What is the city where you want to collect zips? :")
    stateCode :str = input("What is the state where you want to collect zips?\n(This is optional you can just input an empty response, please respond with a state abbreviation) :")
    countryCode :str = input("What is the country code of the country where you want to collect zips? :")

    return mappingApi.ZipFetch(apikey).getZipByCity(city, countryCode, stateCode)


def main():
    output :list[int] = []

    while(not output):
        print("Would you like to get zip codes by radius, or by city?")
        choice = input("response with \"radius\" or \"city\"\n").upper()

        if(choice == "RADIUS"):
            output = getRadiusZips()
        elif(choice == "CITY"):
            output = getCityZips()
        
        if (not output):
            print("\nERROR INVALID RESPONSE\n")

    print(output)

    

if __name__ == "__main__":
    main()