def record():
    name = input("What is your name:")
    father_name = input("What is your father name:")
    print(name,father_name.upper(),sep="|")

record()

def records():
    city = input("What is your city name:")
    country = input("What is your country name:")
    print(city,country.title(),end=">>>>")


records()