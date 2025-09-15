try:
    num = int(input("enter a number"))

    if num > 0:
        print("positive number")
    elif num < 0:
        print("Negative number:")
    elif num == 0:
        print("Zero")

except:
    print(" Galat number ")