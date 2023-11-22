# top_weapons_2_test

def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    if (weapon in top_weapons):
        return True
    else:
        return False
#        in_list = True
#         print(f"in_list = {in_list}")
#         return in_list




my_weapon = "silver bow"

in_list = is_top_weapon(my_weapon)

print(f"OUT OF FUNCT - {my_weapon} is in the top list {in_list}")

print(f"OUT OF FUNCT - {in_list}")



''' print(f"manual entering "silver bow" in top_weapons")
    y = ("silver bow" in top_weapons)
    print(f"y is {y}")

    print(f"in function now")
    print(f"weapon is {weapon}")

    in_list = True


    return in_list
'''

'''    
    print(f"{weapon} in top_weapons is {weapon}")
    z = {weapon}
    x = z in top_weapons
    print(f"x is {x}")
'''