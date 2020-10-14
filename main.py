class PascalList:
    def __init__(self, lst):
        self.lst = lst

    def __setitem__(self, key, value):
        if len(self.lst) >= key:
            self.lst[key - 1] = value
        else:
            self.lst.append(value)

    def __getitem__(self, item):
        return self.lst[item - 1]

    def __str__(self):
        return f'{self.lst}'

