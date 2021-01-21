import random
all_words = "all the words in the world".split()
def get_random_word():
    return random.choice(all_words)
def get_unique_words():
    list_set = []
    while(len(list_set) != 1000):
        list_set.append(get_random_word())

    tmp_set = set(list_set)
    print(tmp_set)
    
get_unique_words()
