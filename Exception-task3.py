try:
    age = int(input("Enter your age:"))

    if age >=18:
        print("Adult")
    elif age <=18:
        print("not an adult")
except:
    print("Galat ha")