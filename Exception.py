try:
    tem = int(input("Enter the temprature"))

    if tem > 30:
        print("It\'s hott")
    elif tem < 30:
        print("It\'s cool")

except:
    print("Galat temperature")

finally:
    print("Temperature Acha ha ")