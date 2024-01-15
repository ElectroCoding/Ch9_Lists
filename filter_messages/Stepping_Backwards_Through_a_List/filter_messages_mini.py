# filter_messages_mini

'''
def filter_messages(comment):
    for i in range(0, len(comment)):
        if i == "3":
            del [i]
    return         

'''


comment = [
    [0, 1, 2],
    [ 3, 4, 5],
    [ 6, 7, 8, 9, 10, 11]
]

print()
print(comment)
  


#  clean_out = filter_messages(comment)

for i in range(len(comment)-1, -1, -1):
    print()
    print(f"i = {i} and the value is {comment[i]}")
    if comment[i] == 9:
        print(f"this number {comment[i]} is a Bad number ***-***")
        print(comment)
      
        
        del comment[i]
 #       i = i+1
        
    else: 
        print("this is not a bad number")
        print(comment)




#            del comment[i]
print()

print(comment)

