valueone = 0
valuetwo = 0
result = 0

def takeinput():
    global valueone,valuetwo
    valueone = int(input("enter first number:"))
    valuetwo = int(input("enter second number:"))
def Addvalues():
    global result
    result = valueone +valuetwo
def showresult():
    global result
    print("the result is "+str(result))


takeinput()
Addvalues()
showresult()