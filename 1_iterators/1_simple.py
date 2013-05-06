# a list of numbers that we will use
# throughout this example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# simply iterate over the list of
# numbers and print each element
for number in numbers:
    print number

# create an iterator object from
# the list of numbers
i_numbers = iter(numbers)

# <listiterator object at 0x10e5fd610>
print i_numbers

# 1
print i_numbers.next()

# print the remaining 2-10
for i in range(9):
    print i_numbers.next()

# throws a StopIteration exception
# meaning that there are no items left
# for the iterator to iterate
try:
    print i_numbers.next()
except StopIteration:
    print 'StopIteration thrown'

# in order to use the iterator again
# we must re-create it
i_numbers = iter(numbers)
for number in i_numbers:
    print number
