try:
    file_name = input("Enter file name")
    read_file = open(file_name,"Hello")
    print(file_name)

except:
    print("file nahi mil rahi")
finally:
    print("program end ho gya")