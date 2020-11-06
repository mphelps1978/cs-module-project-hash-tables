# expensive calcluation on the fly

import math

lookup_table = {}

def inverse_root(n):
  return 1/math.sqrt(n)

for i in range(1, 1000):
  lookup_table[i] = inverse_root(i)


# rainbow table
## hash common passwords ahead of time
## precompute table for cachiing output of crypto-hash functions
### usually for cracking pw hashes

# hashing function for pws should be slow



