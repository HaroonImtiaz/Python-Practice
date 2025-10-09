try:
    def info():
        name = input("Tell me what is your name :")
        father_name = input("Tell me what is your father name :")
        age = int(input("Tell me what is your age :"))
        print("your name is :",name," Your father name is :",father_name,"your age is :",age)

    def student_info():
        marks = int(input("Enter your marks :"))
        Grade = input("Enter your Grade :")
        if Grade == "A":
            print("Excellent")
        elif Grade == "B":
            print("Better")
        elif marks <50:
            print("Fail")

    info()
    student_info()

except:
    print("Please enter a valid input")

finally:
    print("Thank you")