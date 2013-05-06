# for a normal list it will iterate
# over each element
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print number

i_numbers = iter(numbers)
print i_numbers
for number in i_numbers:
    print number

# a tuple is the treated the same
# as a list
number_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for number in number_tuple:
    print number

i_number_tuple = iter(number_tuple)
print i_number_tuple
for number in i_number_tuple:
    print number

# with a dict we will end up iterating
# over the keys instead of the values
number_hash = {'one': 1,
               'two': 2,
               'three': 3,
               'four': 4,
               'five': 5,
               'six': 6,
               'seven': 7,
               'eight': 8,
               'nine': 9,
               'ten': 10}
for key in number_hash:
    print key

i_number_hash = iter(number_hash)
print i_number_hash
for key in i_number_hash:
    print key
