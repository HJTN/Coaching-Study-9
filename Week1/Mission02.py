sentence = "way a is there will a is there where"

def reverse_sentence(sentence):
    words = sentence.split()
    return ' '.join(words[len(words)::-1])

print(reverse_sentence(sentence))