# splitting_a_SINGLE_string_on_whitespace_and_Removing_the_word_Dang

print()
print("=====================================================")








# now check for the word "damn"

def filter_messages(messages):
       
    print(f"The message sent is \"{messages}\"")


    bad_count = 0
    i = -1

    words = messages[i].split()

    # This splits the message up into separate items. The DEFAULT separator is whitespace.

    print()
    print(f" The message Split into separate items is {words}")
    print()

    print()
    print("======================================================")
    print()

    for x in words:
        i = i+1
        print()
        print(f"x is {x}")
        print()
        if x == "damn":
            print(f"{x} was deleted")
            del words[i]
            bad_count = bad_count + 1
            i = i+1
       
    new_String = " ".join(words)
    print()
    print(new_String)
    print()








    print()
    print("Exiting Function")
    print()

    print()
    print("======================================================")
    print()


    return new_String, bad_count

   
       




my_String = "the damn happy dog smiled"

new_String, bad_count = filter_messages(my_String)

print()
print("======================================================")
print()

print(f" The NEW message is - {new_String}")


print(f"The Bad Count is {bad_count}")
print()












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