# trim_strongholds_Test_YetAgain



strongholds = [
            "Rivendale",
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
            "Mordane",
            "Gondolin",
        ]


print(f"original trim_strongholds is {len(strongholds)} {strongholds}")
print()


master_list = strongholds

del strongholds[0]

print(f"New trim_strongholds is {len(strongholds)} {strongholds}")
print()



del strongholds[:-2]

print(f"New trim_strongholds is {len(strongholds)} {strongholds}")
print()

print(f"Compare =====================")

print(master_list[1:4])


