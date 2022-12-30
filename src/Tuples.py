# Tuples are immutable 

coordinates = (4, 5)
print(coordinates[1])

# coordinates[1] = 6    # Not allowed (Tuple elements cannot be modified)

List_of_Tuples = [(4, 5), (6, 7), (20, 78)]
print(List_of_Tuples)

# Unless and until we add comma after the only element in the tuple,
# Python will treat it as a string
SingleElementTuple = ("Hello",) 
print(SingleElementTuple)
AnotherSingleElementTuple = ("Hi")
print(AnotherSingleElementTuple[0]) # returns 'H' as this tuple was treated as a string