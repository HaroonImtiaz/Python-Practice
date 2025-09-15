try:
    choice = int(input("enter a number"))

    if choice == 2:
        print("The number is 2")
    else:
        print("The number is not 2")
except:
    print("Use the correct information")
finally:
    print("This statement is run finally")