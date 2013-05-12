import random


def my_func():
    print '== my_func =='
    numbers = []
    for i in range(5):
        num = random.random()
        print 'generated: %s' % num
        numbers.append(num)
    return numbers


def my_generator():
    print '== my_generator =='
    for i in range(5):
        num = random.random()
        print 'generated: %s' % num
        yield num


for num in my_func():
    print 'got: %s' % num

for num in my_generator():
    print 'got: %s' % num
