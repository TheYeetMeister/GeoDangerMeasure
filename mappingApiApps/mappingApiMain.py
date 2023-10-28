import mappingApi

def getRadiusZips() -> list[int]:
    apikey :str = input("What is your Apikey? :")
    originZip :str = input("What is the origin of your radius (please respond with a zip)? :")
    radius :str = input("What is the radius in which you want to collect zips? :")
    countryCode :str = input("What is the country code of the country where you want to collect zips? :")

    return mappingApi.ZipFetch(apikey).getZipByRadius(originZip, radius, countryCode)

def main():
    output :list[int] = []

    while(not output):
        print("Would you like to get zip codes by radius, or by city?")
        choice = input("response with \"radius\" or \"city\"\n").upper()

        if(choice == "RADIUS"):
            output = getRadiusZips()
        elif(choice == "city"):
            output = getCityZips()
        else:
            print("\nERROR INVALID RESPONSE\n")

    

if __name__ == "__main__":
    main()