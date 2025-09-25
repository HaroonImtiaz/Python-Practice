def get_info():
    global name,marks
    name = input("What is your name? ")
    marks = int(input("Please enter your marks :" ))

def pass_fail():
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")


def grade_system():
    if marks >80:
        print("Grade A")
    elif marks > 60 :
        print("Grade B")
    elif marks > 40:
        print("Grade C")
    else:
        print("Fail")

get_info()
pass_fail()
grade_system()