name = ["HammadMaqbool","basit","Lubna","Nadeem","shairkhan"]
counter = 0
for myname in name:
    counter += 1
    if counter == 1:
        print(str(counter)+"st Name is "+myname)
    elif counter == 2:
        print(str(counter)+"nd Name is "+myname)
    elif counter == 3:
        print(str(counter)+"rd Name is "+myname)
    else:
        print(str(counter)+"th Name is "+myname)
