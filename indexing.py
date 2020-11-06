records = [
  ("Tara", "Web"),
  ("Mike", "Web"),
  ("Kyle", "Web"),
  ("Janessa", "Web"),
  ("Adrian", "Web"),
  ("Cai", "DS"),
  ("Chris", "DS"),
  ("Craig", "iOS")
]

# How can we show in O(1) everyone in a particular track?


# build an index on a particular attribute (indexing on)

# index on the track - make the track the key, and the value as a list, append the names to the list

def build_index(records):
  idx = {}
  for name, track in records:
    if track in idx:
      idx[track].append(name)

    else:
      idx[track] = [name]

  return idx


idx = build_index(records)

print(idx["DS"])
print(idx["Web"])
print(idx["iOS"])