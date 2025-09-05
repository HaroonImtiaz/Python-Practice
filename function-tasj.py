def Abc(valueone, valuetwo):
    sum = valueone + valuetwo
    sub = valueone - valuetwo
    product = valueone * valuetwo
    return sum, sub, product


list_of_results = []

list_of_results = Abc(10,20)
print("The Sum is "+str(list_of_results[0]))
print("The Subtraction is "+str(list_of_results[1]))
print("The Product is "+str(list_of_results[2]))
