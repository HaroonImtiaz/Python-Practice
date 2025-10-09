try:
    for i in range(4):
        name = input("Enter your name :")
        age = int(input("Enter your age :"))

    def name ():
        if name == "Haroon":
            print("Your name is Haroon")
        else:
            print("This is not your name")

    def age():
        if age >18:
            print("your age is greater then 18")
        else:
            print("your age is less than 18")

    name()
    age()
except:
    print("please enter a valid input")

finally:
    print("Thanks")