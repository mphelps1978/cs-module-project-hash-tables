# Does a hashtable preserve order?
## No
### Why?
#### The hash function hashes the index.
##### Takes the key and returns a random index

# sets, dictionaries, objects, hash maps - All do not preserve order

# Can you sort a hashtable? (Or simmilar data structures (Objects, hash map, dictionary, etc.. ))
## Go to the index, and sort the LL?


# What if we got a list based on the dictionary?

my_dict = {
  'a': 1,
  'f00': 'bar',
  'qux' : 'izzy',
}

# a list-like object - actually an iterator
my_dict.items()

dict_list = list(my_dict.items())

dict_list.sort()

# Sort, by default goes in ascending order, AKA Normak alphabetical
## to reverse:
dict_list.sort(reverse = True)

# Sort, by defaut uses the first item in each tuple to sort (key)
# if we want to sort by value
dict_list.sort(key = lambda tuple_pair: tuple_pair[1])

"""
Lambda explained:

It's a HOF..

in JS:
x => x * x
x, y => x * y

in Python:
lambda x: x * x
lambda x, y: x * y

map(lambda x: 2, [1, 2, 3, 4])
<map object at 0x0000013B8387A9D0>

list(map(lambda x:  x * 2, [1, 2, 3, 4]))
[2, 4, 6, 8]
"""