name = input("Enter your name: ")
repeated = set()

for char in name:
    if name.count(char) > 1 and char not in repeated:
        print("Repeated character:", char)
        repeated.add(char)