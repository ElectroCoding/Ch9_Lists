# trim_strongholds_Test



def trim_strongholds(strongholds):

    print(f"original trim_strongholds is {len(strongholds)} {strongholds}")
    print()

    del strongholds[-1:2]
   

    print(f"New trim_strongholds is {len(strongholds)} {strongholds}")
    print()

    return trim_strongholds

strongholds = [
            "Rivendale",
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
            "Mordane",
            "Gondolin",
        ]

trimmed_list = trim_strongholds(strongholds)

