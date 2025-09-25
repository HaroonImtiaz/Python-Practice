try:
    def even_odd():
        number = int(input("Enter your number:"))
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")

    even_odd()

    def positive_negative():
        number = int(input("Enter your number:"))
        if number > 0:
            print("Positive number:")

        else:
            print("Negative number:")

    positive_negative()

    def compare_number():
        number = int(input("Enter your number:"))
        if number > 10:
            print("Greater")
        if number < 10:
            print("Smaller")

    compare_number()

    def check_range():
        number = int(input("please enter number between 1 to 100:"))
        if number >=1 and number <= 100:
            print("The number is between 1 to 100:")
        else:
            print("The number is not between 1 t0 100")
    check_range()

except:
    print("Please give the correct input")

finally:
    print("Program is run successfully")