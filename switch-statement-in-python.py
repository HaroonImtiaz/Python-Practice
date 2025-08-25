alphabet=input("pleace enter alphabet a-e-i-o-u")
match alphabet:
    case 'a' |'e' |'i'|'o'|'u':
        print("Yes, you entered a vowel")
    case _:
        print("not a vowel letter")
