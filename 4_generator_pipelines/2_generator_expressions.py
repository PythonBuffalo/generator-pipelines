numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_pipeline = (num + 2 for num in numbers)
numbers_pipeline = (num * 3 for num in numbers)

for num in numbers_pipeline:
    print 'Final: %s' % num
