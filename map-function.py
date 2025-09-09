small_list = ['a','c','d','e']

def case_changer(character_value):
    return character_value.upper()
final_value = map(case_changer, small_list)
print(list(final_value))