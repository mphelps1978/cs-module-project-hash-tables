with open("robin.txt") as f:
  words = f.read()

  def create_histogram(words):
    ignored = '":;,.-+=/\\|[]{}()*^&'

    filtered = ''.join(filter(lambda x: x not in ignored, words))

    word_list = filtered.split()

    largest = max(word_list, key = lambda s: (len(s), s))

    count = {}

    for word in word_list:
      new_word = word.lower()
      if count.get(new_word) is None:
        count[new_word] = 1

      else:
        count[new_word] = count[new_word] + 1

    sorted_words = sorted(count.items(), key = lambda x: x[1], reverse = True)

    for word, count in sorted_words:
      white_space = len(largest) - len(word)
      print(word + ' ' * white_space + count * '#')

create_histogram(words)




