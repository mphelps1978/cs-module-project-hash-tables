# memoization, closely related to dynamic programming

# when using a hashtable
## key is the input (what you have)
## value is the calculation

# fibonacci sequence
## function that will rethrn nth item in the sequence


# Doiing this Recursively:
## need base case
## progress towards the base case

cache = {}
def fib(n):

  # base case
  if n == 0 or n == 1:
    return n

  else:
    if n in cache:
      return cache[n]
    else:
      cache[n] = fib(n - 1) + fib(n - 2)

print(fib(4))




