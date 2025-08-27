Random = ["0325678807","03407899087","03481233456"]
for number in Random:
    if len(number) == 11 and number.startswith("0"):
        Haroon = number
        ZeroRemovedVersion = Haroon[1:]
        CountryCodeAdded = "+92"+ZeroRemovedVersion
        print(CountryCodeAdded)
    else:
        print("Not a valid number")

        #hello
