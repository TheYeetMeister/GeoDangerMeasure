import mappingApi

def main():
    output :str = ""

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