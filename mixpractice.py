try:
    name = input("What is your name:")
    age = int(input("What is your age:"))

    if age >= 18:
        if age >= 60:
            print(f" Hello {name} your age is {age} and you are senior citizen and you are elligible to vote")
        else:
            print(f" Hello {name} your age is less than 18 you are adult elligible to vote")
    elif age < 18:
        print(f" Hello {name } you are not elligible to vote")
except:
    print("Wrong input")

finally:
    print(" Information Complete")