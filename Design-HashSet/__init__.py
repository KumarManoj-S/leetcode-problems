
class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.set = [[-1] * 1 for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self.hash(key)

        if not self.contains(key, index):
            self.set[index].append(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)

        if self.contains(key, index):
            self.set[index].remove(key)

    def contains(self, key: int, index=None) -> bool:
        index = index if index else self.hash(key)
        return key in self.set[index]


obj = MyHashSet()
obj.add(1)
obj.remove(2)
print(obj.contains(1))
print(obj.contains(2))
obj.add(3)
obj.add(3)
obj.remove(3)
print(obj.contains(3))

