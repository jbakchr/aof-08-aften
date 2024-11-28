def count_words(sentence):
    words = sentence.split()
    return len(words)


print(count_words("Hello world! How are you?"))
print(count_words(""))
