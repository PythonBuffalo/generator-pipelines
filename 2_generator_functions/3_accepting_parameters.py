import random


def my_generator(count):
    for i in range(count):
        yield random.random()


for num in my_generator(10):
    print num


def lower_words(words):
    for word in words:
        yield word.lower()

words = ['HERE', 'ARE', 'SOME', 'ANGRY', 'WORDS']
for word in lower_words(words):
    print word
