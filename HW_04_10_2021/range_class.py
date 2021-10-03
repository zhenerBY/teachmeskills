class rg:
    """Замена RANGE (generator)"""

    def __init__(self, start, stop=None, step=None):
        if step == 0:
            raise ValueError("rg() arg 3 must not be zero")
        if stop == step and stop == None:
            stop, start, step = start, 0, 1
        elif step == None:
            step = 1
        self.start = start
        self.stop = stop
        self.step = step

    def __getitem__(self, index):
        if isinstance(index, slice):
            if index.start == None:
                start = self.start
            else:
                start = self.__getitem__(index.start)
            if index.stop == None:
                stop = self.stop
            else:
                stop = self.__getitem__(index.stop)
            if index.step == None:
                step = self.step
            else:
                step = index.step
            return print(start, stop, self.step * step)
        else:
            if index > self.__len__() - 1:
                raise ValueError("range object index out of range")
            elif index < -self.__len__():
                raise ValueError("range object index out of range")
            if index < 0:
                index = self.__len__() + index
            n = self.start
            it = 0
            while it < index:
                n += self.step
                it += 1
            return n

    def __len__(self):
        if self.step > 0:
            if (self.stop - self.start) // self.step >= 0:
                return (self.stop - self.start) // self.step
            else:
                return 0
        else:
            if abs(self.start - self.stop) // abs(self.step) >= 0:
                return abs(self.start - self.stop) // abs(self.step)
            else:
                return 0

    def __repr__(self):
        if self.step == 1:
            return f'rg({self.start}, {self.stop})'
        else:
            return f'rg({self.start}, {self.stop}, {self.step})'

    def __iter__(self):
        n = self.start
        if self.step > 0:
            while n < self.stop:
                yield n
                n += self.step
        elif self.step < 0:
            while n > self.stop:
                yield n
                n += self.step


print(rg(-10, 22, 1))

for i in rg(-10, -20, -2):
    print(i)

print(len(rg(-10, -55, -2)))
