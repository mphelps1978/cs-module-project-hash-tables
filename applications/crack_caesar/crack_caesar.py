# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("ciphertext.txt") as f:
  words = f.read()

  def crack_caesar(code):

    frequencies = ('E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z')

    count = {}
    key = {}
    decrypted = ''

    #First, get the count of the items in code

    for c in code:
      if c in frequencies:

        if count.get(c) is None:
          count[c] = 1

        else:
          count[c] = count[c] + 1

    sorted_count = sorted(count.items(), key = lambda x: x[1], reverse = True)

    for i in range(len(frequencies)):
      key[sorted_count[i][0]] = frequencies[i]

    for c in code:
      if c in frequencies:
        decrypted += key[c]

      else:
        decrypted += c

    return decrypted

print(crack_caesar(words))