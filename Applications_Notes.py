import random
import hashlib

# Birthday Paradox
# There likely will be a collision of birthdays

# Can we avoid them by using a very large array?

#sha256 always produces a unique output, but we modify the output so we still get collisions
def our_hash(key, num_buckets):
  key_bytes = f'{key}'.encode()
  hashed_key = int(hashlib.sha256(key_bytes).hexdigest(), 16)
  return hashed_key % num_buckets
  

def how_many_before_collision(num_buckets):
  while True:
    # Make a bunch of random keys
    hashed_keys = set()
    tries = 0
    key = random.random()
    
    # Hash them, modulo them by the number of buckets (size of the array)
    hashed_key = our_hash(key, num_buckets)
    
    if hashed_key in hashed_keys:
      break
      
    else:
      hashed_keys.add(hashed_key)
      tries += 1
  
  print(f'Collision! Tries: {tries} before collision')
# Rinse, Repeat and see how far we get before a collision

# random.random()


