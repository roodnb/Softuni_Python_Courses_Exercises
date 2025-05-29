from typing import NamedTuple, Any


class Pair(NamedTuple):
    key: Any
    value: Any


class Deleted:
    pass


class HashTable:
    DELETED = Deleted()

    def __init__(self, capacity=4):
        self.capacity = capacity
        self._array: list[Pair | None | HashTable.DELETED] = [None] * self.capacity

    @property
    def array(self):
        return {pair for pair in self._array if pair not in (None, self.DELETED)}

    @property
    def keys(self):
        return {pair.key for pair in self.array}

    @property
    def values(self):
        return [pair.value for pair in self.array]

    def hashing(self, key):
        return sum(ord(ch) for ch in str(key)) % self.capacity

    def __setitem__(self, key, value):  # zimame tva koeto ni vryshta _probe kato index i ako nqma nishto zapisvame a ako ima na vsichkite nehsto _resize i
                                        # rekursivno vikame setitem s reda self[key] = value
        # self._array[self.hashing(key)] = Pair(key, value)
        for index, pair in self._probe(key):
            if pair is None or pair.key == key:
                self._array[index] = Pair(key, value)
                break
        else:
            self._resize()
            self[key] = value

    def __getitem__(self, key):
        for _, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is self.DELETED:
                continue
            if pair.key == key:
                return pair.value
        raise KeyError(key)

    def __delitem__(self, key):
        for index, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is self.DELETED:
                continue
            if pair.key == key:
                self._array[index] = self.DELETED
                break
        else:
            raise KeyError(key)

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def add(self, key, value):
        self[key] = value

    def pop(self, key, default=None):
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            if default is not None:
                return default
            raise

    def __len__(self):
        return len(self.array)

    def __contains__(self, item):
        try:
            self[item]
        except KeyError:
            return False
        else:
            return

    def __str__(self):
        result = []
        for k, v in self.array:
            result.append(f"{k!r}: {v!r}")
        return "{" + ", ".join(result) + "}"

    def _probe(self, key):  # wzimame tva koeto ni vryshta kato indez hashing , i proverqvame dali ima na nego mqsto neshto i spira.
        index = self.hashing(key)
        for _ in range(self.capacity):
            yield index, self._array[index]
            index = (index + 1) % self.capacity

    def _resize(self):  # suzdavame nov obekt , udvoqvame tablicata , prezapisvame starata tablica i na tekushtiq ni obekt mu kazwame
                        # kapaciteta ti stava kato toq na noviq obekt , a _array-a ti stava kato toq nq novia obekt
        copy_table = HashTable(capacity=self.capacity * 2)
        for k, v in self.array:
            copy_table[k] = v
        self.capacity = copy_table.capacity
        self._array = copy_table._array


table = HashTable()

table["name"] = "Peter"
table["age"] = 25
print(table)  # works due to the __str__method
print(table.get("name"))
print(table["age"])
print(len(table))
print(table.keys)  # works because of the property keys
print(table.values)  # works because of the property val
print(table.array)  # works because of the property array - realno mamim krainiq potrebitel che vijda _array no realno vijda property-to koeto si e otdelno to _array
print("age" in table)  # works because of the __contains__ dunder method
print(table.pop("age"))
