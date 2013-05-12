words = ['LOOK', 'MA', 'I', 'AM', 'SHOUTING']
lowered = [word.lower() for word in words]
for word in lowered:
    print word

numbers = [1, 2, 3, 3, 2, 1, 4, 5, 4, 3, 2, 1]
unique_numbers = set([num for num in numbers])
print unique_numbers
