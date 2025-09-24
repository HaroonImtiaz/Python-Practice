def student_info():
    name = input("What is your name:")
    father_name = input("What is your father name:")
    print(name,father_name.upper(),sep="|")

student_info()

def student_info2():
    age = int(input("What is your age:"))
    class_name = input("What is your class name:")
    print(age,class_name,end="*****")

student_info2()

def sentence():
    sentence = input("Please enter a sentence:")
    print(sentence.count("a"))
    print(sentence.replace("a","@"))

sentence()

def student_info3():
    city = input("Please enter your city name:")
    country = input("Please enter your country name:")
    print(city,country.title().startswith("P"))

student_info3()

