for i in range(1, 20, 15):
    print(i)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(a))


class srange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()



