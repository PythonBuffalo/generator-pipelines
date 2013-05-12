class FilterPipeline(object):
    def __init__(self):
        self._filters = []

    def add_filter(self, filter):
        self._filters.append(filter)

    def read(self, iterable):
        pipeline = iterable
        for filter in self._filters:
            pipeline = filter(pipeline)

        for element in pipeline:
            yield element
