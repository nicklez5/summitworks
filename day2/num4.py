list_words = []
while(True):
    word_value = input("Enter the word\n")
    if(len(word_value) != 0):
        if(word_value not in list_words):
            list_words.append(word_value)
    else:
        for i in list_words:
            print(i)
        break

