try:
    choice = int(input("enter a number"))

    if choice == 1:
        print("you pressed one")
    else:
        print("pressed number is not one")
except:
    print("there is something wrong")
else:
    print("This is the else running here.")
finally:
    print("this is the code finally")