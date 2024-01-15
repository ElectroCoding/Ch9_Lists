# splitting_string_on_whitespace

print()
print("=====================================================")








# now check for the word "damn"

def filter_messages(messages):
    # my_list1 = []
    # my_list2 = []

    print(messages)
    print(len(messages))

    for i in range(1, len(messages)):

        words = messages[i]

        # words2 = messages[1]

        # words = messages.split()
        print()
        print(words)
        print()
        # print(words2)

        # my_list1 = words1

        
        
        print()
        print("======================================================")
        print()

        for x in words:
            print()
            print(f"x is {x}")
            print()
            if x == "damn":
                print(f"{x} was deleted")
                del x
                bad_count += 1

        my_list1 = " ".join(words)
        print()
        print(my_list1)




        # my_list1.append(my_list1)
        # my_list2.append(bad_count)


        
        print()

        print()
        print("Exiting Function")
        print()

        print()
        print("======================================================")
        print()
        


    return my_list1

    
        




my_String = ["the damn happy dog smiled", "the frisky cat"]

mu_list1 = filter_messages(my_String)

print()
print("======================================================")
print()

print(mu_list1)








