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
