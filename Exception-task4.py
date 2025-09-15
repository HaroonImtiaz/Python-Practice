try:
    marks = int(input("Enter your marks:"))

    if marks >= 50:
        print("pass")
    elif marks <= 50:
        print("fail")

except:
    print("galat number")