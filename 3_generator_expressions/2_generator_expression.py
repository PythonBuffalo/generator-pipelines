words = ['LOOK', 'MA', 'I', 'AM', 'SHOUTING']
lowered = (word.lower() for word in words)
print lowered
print lowered.next()
for word in lowered:
    print word

try:
    lowered.next()
except StopIteration:
    print 'none left to iterate'


numbers = [1, 2, 3, 3, 2, 1, 4, 5, 4, 3, 2, 1]
# NOTICE: no surrounding parentheses
unique_numbers = set(num for num in numbers)
print unique_numbers
