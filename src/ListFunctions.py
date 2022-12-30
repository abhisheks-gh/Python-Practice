# List functions

movies = ["Mission Impossible 6", "Social Network", "Inception", "Snowden", "Spiderman", "3 Idiots"]
more_movies = ["Superman", "Batman"]

# append() -> adds item to the list
movies.append("Extraction")

# insert(indexPosition, item) -> insert item at a particular index
movies.insert(2, "Border")

# extend() -> appends two lists
movies.extend(more_movies) 
print(movies)

# remove() -> removes an item
movies.remove("Superman")
print(movies)

# index() -> if element is present then returns its index else ValueError
print(movies.index("Batman"))

# sort() -> sorts the list
print(movies.sort())   

# pop() -> pops out the last element
print(movies.pop())
print(movies)

# clear() -> empty the list
print(movies.clear())   # returns None
print(movies)           # returns []

# reverse() -> to revere the list
more_movies.reverse()
print(more_movies)

# copy()
duplicateList = more_movies.copy()
print(duplicateList)