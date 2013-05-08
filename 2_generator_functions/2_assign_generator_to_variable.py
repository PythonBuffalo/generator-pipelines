import random


def my_generator():
    for i in range(5):
        yield random.random()


gen = my_generator()
print gen

print gen.next()

for num in gen:
    print num

try:
    gen.next()
except StopIteration:
    print 'no more items left'
