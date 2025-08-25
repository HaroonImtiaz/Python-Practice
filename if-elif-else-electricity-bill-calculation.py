units = int(input("please enter the electricity Bill"))
if units <= 100:
    print("Rs 5 per unit")
elif units <= 200:
    print("Rs 7 per unit")
elif units <= 300:
    print("Rs 10 per unit")
else:
    print("Rs 15 per unit")
