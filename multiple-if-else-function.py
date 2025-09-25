def check_age():
    age = int(input("Enter your age:"))
    if age >= 18:
        print("you can vote")
    else:
        print("you can\'t vote")

check_age()

def check_marks():
    marks = int(input("Enter your marks"))
    if marks >= 50:
        print("Pass")
    else:
        print("Fail")

check_marks()


def check_city():
    city = input("Enter your city")
    if city == "Kotli":
        print("Wellcome to Kotli")
    else:
        print("Different city")

check_city()