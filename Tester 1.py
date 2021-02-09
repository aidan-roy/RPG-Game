y = -1

stuff = "stuff"


def reverse_me(word,x):
    new_word = ""
    for i in range(len(word)):
        new_word = new_word + (word[x])
        x = x - 1
    print (new_word)

reverse_me(stuff, y)