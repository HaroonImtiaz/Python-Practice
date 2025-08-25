age = int(input("please enter your age:"))
if age >= 18:
    cnic = input("Do you have cnic yes/no")
    if cnic == "yes":
        cnic_type = input("is your cnic original yes/no")
        if cnic_type == "yes":
            print("eligible for licence")
        else:
            print("fake licence")
    else:
        print("cnic required")
else:
    print("not eligible for licence")
