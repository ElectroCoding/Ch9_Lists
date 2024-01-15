capitals = {'UK': 'London', 'France': 'Paris', 'Germany': 'Berlin'}


print (capitals)
print ("========================")
print()

del capitals['UK'] 
# - a key is specified
# - the associated Key-Value pair is removed
# - square brackets are used since it is a Keyword

print (capitals)
print ("========================")
print()

capitals.pop('Germany') 
# - a key is specified
# - the associated Key-Value pair is removed
# - regular brackets are used since "pop" is a method


print (capitals)
print ("========================")
print()

capitals.popitem()
# - nothing is specified, the method brackets are empty
# - a RANDOM Key-Value pair is removed
# - regular brackets are used since "popitem" is a method


print (capitals)
print ("========================")
print()


