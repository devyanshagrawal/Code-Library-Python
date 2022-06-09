class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # def add(self, key, val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val    

    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]    

t = HashTable()
# t.add('index 9', 99)

# print(t.arr)

t['index 10'] = 19

print(t['index 10'])
