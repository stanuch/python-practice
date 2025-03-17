class KVdata:
    def __init__(self, data):
        self.data = data
        self.keys = list(data.keys())
        self.index = 0

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.keys):
            current_key = self.keys[self.index]
            self.index += 1
            return current_key, self.data[current_key]
        else:
            raise StopIteration

    def __contains__(self, key):
        return key in self.data

data = {'Joker': 10, 'Spider-Man': 15, 'Batman': 30}
obiekt = KVdata(data)

print(obiekt.__next__())
print(obiekt.__next__())
print(obiekt.__next__())
print("Spider-Man" in obiekt)
print(obiekt["Batman"])