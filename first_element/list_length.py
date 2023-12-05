# list_length

def first_check(listings):

    print(f"Length of listings is {len(listings)}")

    print(listings)

    for i in range(listings[]):
    
        if len(listings[0]) == 0:
            result = "ERROR"
            return listings[0], result
        else:
            return listings[0]


listings = [(["Iron Ore", "Iron Bar", "Scimitar"], "Iron Ore"),
([], "ERROR"),
(["Apple", "Banana", "Cherry"], "Apple"),
([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]),
([False, True, False], False),
([None, "None", 0], None),]



#  listings = ([], [2, 5], ["sword", "dagger"], [22, 3, 4], [])


print(f"Length of listings is {len(listings)}")
 
print()
print(f"=================================")
print()



ans = first_check(listings)

print(ans)



