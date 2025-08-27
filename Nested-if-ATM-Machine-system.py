card_valid = input("please enter your valid card no yes/no:")
if card_valid == "yes":
    pin = int(input("Please enter your four digit pin:"))
    if pin == 4444:
        print("Transaction allowed")
    else:
        print("wrong pin")
else:
    print("invalid card")
