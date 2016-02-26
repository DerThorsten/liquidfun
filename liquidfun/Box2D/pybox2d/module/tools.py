class GenericB2dIter(object):
    def __init__(self, currentBody):
        self.currentBody = currentBody
    def __next__(self):
        return self.next()
    def __iter__(self):
        return self
    def next(self):
        if self.currentBody is None:
            raise StopIteration
        else:
            c = self.currentBody
            self.currentBody = c.GetNext()
            return c
