# Lists in Python

# list can store different data types together
# example = [1.2, 56, "Hello"]

movies = ["Mission Impossible 6", "Social Network", "Inception", "Snowden", "Spiderman", "3 Idiots"]
print(movies)
print(movies[2])

print(movies[-1])   # prints "Snowden"

print(movies[2:])   # prints element at index 2 and all elements after that
print(movies[2:4])  # prints elements in the range(2,4); where 4 is exclusive

movies[1] = "Peaky Blinders"
print(movies)