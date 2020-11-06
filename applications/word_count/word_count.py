def word_count(s):
    # define the characters we need to ignore
    ignore = '":;,.-+=/\\|[]{}()*^&'

    # re-write the string to remove the characters to ignore
    filtered_string = ''.join(filter(lambda x : x not in ignore, s))

    # Gets all escaped values (apostrophies, etc..)
    escapes = ''.join([chr(char) for char in range(1, 32)])

    # Takes the escaped values and replaces them all with empty spaces (example: isn\'t becomes isn't)
    words  = filtered_string.translate(str.maketrans(escapes, ' ' * 31)).split(' ')

    count = {}

    for word in words:
        if len(word):
            try:
                count[word.lower()] = count[word.lower()] + 1
            except:
                count[word.lower()] = 1

    return count







if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))