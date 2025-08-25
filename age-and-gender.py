age = int(input("Please enter your age:"))
gender =input("Please enter your gender:")
if age >= 18:
    if gender == "male":
        print("you are an adult male")
    elif gender == "female":
        print("you are an adult female")
if age < 18:
    if gender == "male":
        print("you are a boy")
    elif gender == "female":
        print("you are a girl")
        
