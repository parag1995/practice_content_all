class iter_class:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num <= self.max:
            result = 2*self.num
            self.num += 1
            return result
        else:
            raise StopIteration
# for i in iter_class(5):
#     print(i)

obj = iter_class(5)
# print(next(obj))
for i in obj:
    print(i)
    print(next(i))

