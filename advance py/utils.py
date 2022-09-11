def char_counter(sentence):
    data ={}
    for char in set(sentence):
        data[char]=sentence.count(char)
    return data




def word_counter(sentence):
    data={}
    words = sentence.split()
    for word in set(words):
        data[word]=words.count(word)
    return data