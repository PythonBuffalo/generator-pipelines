class DataContainer(object):
    """A container class for a dict which when
    iterated over will iterate over the values
    in the dict instead of the keys
    """
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data.values())


data = {'some': 'data', 'here': True}
container = DataContainer(data)
for value in container:
    print value

i_container = iter(container)
print i_container
for value in i_container:
    print value

try:
    print i_container.next()
except StopIteration:
    print 'no more items left'
