def add_two(numbers):
    for num in numbers:
        yield num + 2


def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num
        else:
            print 'Skipping: %s' % num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_pipeline = filter_even(add_two(numbers))
for num in numbers_pipeline:
    print 'Final: %s' % num
