class RandomizedSet:

    def __init__(self):
        self.mem = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.mem.append(val)
        self.map[val] = len(self.mem) - 1

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        idx = self.map[val]
        lastVal = self.mem[-1]
        self.map[lastVal] = idx
        self.mem[idx] = lastVal
        del self.map[val]
        self.mem.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.mem)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()