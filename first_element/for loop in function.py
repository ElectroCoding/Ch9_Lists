# for loop in function


def my_listings(listings):
    print()
    print(f"=================================")
    print()
    print()
    # print(f"the first item of the first list is {listings[0][0][0]}")
    print()

    print(f"Length of listings is {len(listings)}")

    print()
    print(f"=================================")
    print()

    for i in range(len(listings)):


        print(f"the first item of the first list is {listings[i[0]]}")
    # print(f"Length of first item of the list is {len(listings[0][0][0])}")
    
        print()
        print(f"=================================")
        print()



listings = [
([[], "ERROR"], [34, 23, 45, 11]),
(["Iron Ore", "Iron Bar", "Scimitar"], "Iron Ore"),
([], "ERROR"),
(["Apple", "Banana", "Cherry"], "Apple"),
([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3]),
([False, True, False], False),
([None, "None", 0], None),]


ans = my_listings(listings)

print(f"the answer is {ans}")