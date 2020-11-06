# Transposition Table:

# Data in one form that needs to be transformed to another form


# Transposition Cipher (Caesar Cipher -> 'rotate' the letter)

# given a string, build a new string by looking up each letter

encode_table = {
   'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

# make function to encode a string:
## iterate through the string
## for every letter, look up it's encoding
## build a new string

def encode(old_string):
  new_string = ''
  for letter in old_string.upper():
    new_string = new_string + encode_table[letter]
  return new_string



# make a decode table so we can decode
# with encode table, keys -> values, values -> keys

# Iterate through encode_table
# for each key/val - Add to new dict with v, k

decode_table =  {}
for key, value in encode_table.items():
  decode_table[value] = key


def encode(old_string):
  new_string = ''
  for letter in old_string.upper():
    new_string = new_string + decode_table[letter]
  return new_string