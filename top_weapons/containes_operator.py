# containes_operator


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
    print(f"this is the weapon sent in from main - {weapon}")

#    print("silver bow" in top_weapons)
#print("silver bow is in top_list")

    print("Start check")

# BADprint ({weapon} in top_weapons)

# BAD print ("weapon" in top_weapons)

    print (weapon in top_weapons)

    print ("End Check")

    x = (weapon in top_weapons)
    print(f"x = {x}")

    return x

my_fav = "silver bow"

ans = is_top_weapon(my_fav)

print(f"{my_fav} is in the list - {ans}")