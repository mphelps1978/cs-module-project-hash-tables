# Web Client cache

# 'client' gets whatever URL we provide

# cache the web page on first request
## on subsequent requests, client gives previous fetch (cache)

# Why?
## Speed
### Particularly for large pages, or slow connections
### Avoid Database Hits

# How to use hash tables to create a client cache?
## AKA Proxy Server

# What should be the key/value?
# value = compiled DOM
# key = fetchdate? URL?
## URL

# check if the URL is in the cache
# if not, fetch and cache

import urllib.request

cache = {}
def web_client(url):
  if url in cache:
    return cache[url]
  else:
    response = urllib.request.urlopen(url)
    data = response.read
    response.close()
    cache[url] = data
    return cache[url]


# What if the website changes? Data in cache would be stale
# How do we control the size of the cache?


