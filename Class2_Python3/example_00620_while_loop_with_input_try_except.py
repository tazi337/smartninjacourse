number = None

while not number:
    try:
        userinput = input("Enter an integer number: ")
        number = int(userinput)
    except:
        print()
        print("Error: ")
        print("Please try again")
        print()
else:
    print("You entered the valid number: ", number)
