def average_calculator(obtainmarks, totalmarks):
    div = lambda X : X/totalmarks
    return div(obtainmarks)*100
obtainmarks = int(input("enter the obtain marks: "))
totalmarks = int(input("enter the total marks: "))
final_average = avarage_calculator(obtainmarks, totalmarks)
print("final average of the marks is "+str(final_average))