import mappingApi

def main():
    print("Would you like to get zip codes by radius, or by city?")
    choice = input("response with \"radius\" or \"city\"\n").upper()

    if(choice == "RADIUS"):

    elif(choice == "city"):

    

if __name__ == "__main__":
    main()