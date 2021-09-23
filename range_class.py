class rg:
    """Замена RANGE (tuple)"""

    def __init__(self, start, stop = None, step = None):
        if stop == step and stop == None:
            stop, start, step = start, 0 , 1
        elif step == None:
            step = 1
        self.start = start
        self.stop = stop
        self.step = step
        list1 = []
        n = start
        if step > 0:
            while n < stop:
                list1.append(n)
                n += step
        elif step < 0:
            while n > stop:
                list1.append(n)
                n += step
        self.tuple = tuple(list1)

    def __getitem__(self, i):
        return self.tuple[i]

    def __len__(self):
        return len(self.tuple)

    def __repr__(self):
        if self.step == 1:
            return f'range({self.start}, {self.stop})'
        else:
            return f'range({self.start}, {self.stop}, {self.step})'



print(rg(-10, 22, 1))
