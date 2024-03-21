class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i < self.start:
            self.i = self.start-1
        self.i += 1
        if self.i % 2:
            self.i += 1
        if self.i > self.end:
            raise StopIteration
        return self.i

en = EvenNumbers(10, 25)
for i in en:
    print(i)