try:
    for i in range(5):
        number = int(input("Enter a number :"))
        print("The square is this number is : ",number * number)
except:
    print("Enter Correct information")
finally:
    print(".........End........")
