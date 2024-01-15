# splitting_string_on_whitespace

print()
print("=====================================================")








# now check for the word "damn"

def filter_messages(messages):
    my_list1 = []
    my_list2 = []

    print(messages)
    print(messages[0])

    print(len(messages))

    bad_count = 0

    for i in range(0, len(messages) - 1):

    
        
        words = messages[i].split()
        print()
        print(words)
        print()

        print()
        print("======================================================")
        print()

        for x in words:
            print()
            print(f"x is {x}")
            print()
            if x == "damn":
                bad_count += 1
            else:
                # print(f"{x} was deleted")
                # del x
                # print(words)
                my_list1.append(x)
                
                # words.remove('damn')
                
                
        print(f" my_list1 after append = {my_list1}")       

        list_after_append = my_list1

        my_list1 = " ".join(my_list1)
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

        


    return my_list1, my_list2, list_after_append

    
        




my_String = ["the damn happy dog smiled", "the frisky cat"]

mu_list1, my_list2, list_after_append = filter_messages(my_String)

print()
print("======================================================")
print()

print(mu_list1, my_list2)
print()
print(f"my_list_append = {list_after_append}")












'''
    words = messages.split()
    for i in range(len(words)-1, -1, -1):
        print()
        print(f"i = {i} and the value is {words[i]}")
        if words[i] == "damn":
            print()

            print("======================================================")
            print()

            print(f" ***-***  this word {words[i]} is a BAD WORD ***-***")
           print("======================================================")
            print()
           print(words)
            my_Index = i
            bad_Word = words[i]
            print()
            print(f" The index of the Bad Word is {i}")
        
            print("======================================================")
            print()
            del words[i]
           i = i+1
            
        else: 
            print("this is not a bad word")
            print(words)


print()
print()

print("=====================================================")

print("=====================================================")

print("=====================================================")

print("=====================================================")
print()
print(f" This is the Bad Word -- \"{bad_Word}\"")
print(f" The Index was at {my_Index}")
print()
print("=====================================================")


#            del words[i]
print("=====================================================")
print()
print(f" These are the Clean words {words}")
print()
print("=====================================================")


new_String = " ".join(words)

print()

print("=====================================================")
print()
print(f" This is the Clean String \"{new_String}\"")
print()
print("=====================================================")


'''