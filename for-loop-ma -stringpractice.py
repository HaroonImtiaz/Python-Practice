text = "machinelearningisfun"
vowels = "aeiouAEIOU"
for char in text:
    if char in vowels:
        if char.lower():
            print(char)
