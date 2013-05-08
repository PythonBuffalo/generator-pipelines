import random


def my_generator(count):
    for i in range(count):
        yield random.random()


for num in my_generator(10):
    print num
