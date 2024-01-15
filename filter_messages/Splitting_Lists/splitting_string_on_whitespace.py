# splitting_string_on_whitespace

print()
print("=====================================================")


my_String = "the damn happy dog smiled"

words = my_String.split()

print(words)

# now check for the word "damn"

for i in range(len(words)-1, -1, -1):
    print()
    print(f"i = {i} and the value is {words[i]}")
    if words[i] == "damn":
        print()

        print("======================================================")
        print()

        print(f" ***-***  this word {words[i]} is a BAD WORD ***-***")
#       print("======================================================")
        print()
#       print(words)
        my_Index = i
        bad_Word = words[i]
        print()
        print(f" The index of the Bad Word is {i}")
      
        print("======================================================")
        print()
        del words[i]
 #       i = i+1
        
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


