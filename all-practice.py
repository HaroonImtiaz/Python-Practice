num = int(input("enter a number"))

if num > 0:
    if num % 2 == 0:
        print("even")
elif num < 0:
    print("negative number")
else:
    print("zero")