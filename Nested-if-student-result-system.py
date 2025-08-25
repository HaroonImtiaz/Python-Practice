marks = int(input("Enter the marks of student :"))
if marks >= 50:
    if marks >= 80:
        print("Grade A")
    elif marks >= 60:
         print("grade B")
    else:
        print("Grade C")
elif marks < 50:
     print("fail")
