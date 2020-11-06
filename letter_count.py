# given a string, count how many times each letter occurs in it
# print by descending order, from most common letter to least common

our_string = "supercalifragilisticexpialidocious"

# loop through the string and place in a dictionary

#UPER
# Understand:
## Spaces and Special Characters?
### Ignore them

# Plan:
## Loop and place in dict
## Use python list sorting methods to sort values descending
##

# Execute

def letter_count(s):
  our_dict = {}

  for letter in s:
    if letter in our_dict:
      our_dict[letter] += 1
    else:
      # ignore non-alpha
      if letter.isalpha():
        our_dict[letter] = 1

  return our_dict

count_dict = letter_count(our_string)

list_dict = list(count_dict.items())

list_dict.sort(reverse = True, key = lambda pair: pair[1])

v_set = set()
for k, v in list_dict:
  if v not in v_set:
    print(v, k)
    v_set.add(v)
  else:
    print(' ', k)


# Review:
## Stretch Goal: print each value only once with every key that has the same value
