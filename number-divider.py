num = int(input("Enter a number:"))
if num > 50:
    if num % 10 == 0:
        print("Greater than 50 and divisible by 10")
    else:
        print("greater than 50 and not divisible by 10")
elif num < 50:
    print("less than 50")
if num == 50:
    print("Equal to 50")
