import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

    word_list = words.split()
    starting_words = []

    def get_words_after(word_list):
        after_words = {}

        for i in range(len(word_list)):
            if i == len(word_list) - 1:
                break

            if word_list[i][0].isupper() or (word_list[i][0] == '"' and word_list[i][1].isupper()):
                starting_words.append(word_list[i])

            if word_list[i] not in after_words:
                after_words[word_list[i]] = [word_list[i + 1]]

            else:
                after_words[word_list[i]].append(word_list[i + 1])

        return after_words

    def make_new_sentence(after_words, starting_words):
        current = random.choice(starting_words)

        while current[-1] not in ('.', '?', '!'):
            if current[-1] == '"' and current[-2] in ('.', '?', '!'):
                break

            print(current, end= " ")
            current = random.choice(after_words[current])
        print(current)







# TODO: construct 5 random sentences
# Your code here

make_new_sentence(get_words_after(word_list), starting_words)
print('')
make_new_sentence(get_words_after(word_list), starting_words)
print('')
make_new_sentence(get_words_after(word_list), starting_words)
print('')
make_new_sentence(get_words_after(word_list), starting_words)
print('')
make_new_sentence(get_words_after(word_list), starting_words)

