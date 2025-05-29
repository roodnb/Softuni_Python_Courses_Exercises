from typing import NamedTuple, Any


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self._array: list = [None] * self.capacity

    @property
    def array(self):
        return {pair for pair in self._array if pair}

    @property
    def keys(self):
        return {pair.key for pair in self.array}

    @property
    def values(self):
        return [pair.value for pair in self.array]

    def hashing(self, key):
        result = hash(str(key))
        return sum(ord(ch) for ch in str(key)) % self.capacity

    def __setitem__(self, key, value):
        self._array[self.hashing(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self._array[self.hashing(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def add(self, key, value):
        self[key] = value

    def __len__(self):
        return len(self.array)


table = HashTable()

table["age"] = 25
table["name_"] = "Peter"

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
