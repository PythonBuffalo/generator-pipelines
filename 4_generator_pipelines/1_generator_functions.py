def first_generator(numbers):
    for num in numbers:
        print 'First Generator: %s' % num
        yield num


def second_generator(numbers):
    for num in numbers:
        print 'Second Generator: %s' % num
        yield num


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_pipeline = second_generator(first_generator(numbers))

for num in numbers_pipeline:
    print 'Final: %s' % num
