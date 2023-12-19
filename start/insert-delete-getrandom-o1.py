class RandomizedSet:

    def __init__(self):
        self.set_ = set()

    def insert(self, val: int) -> bool:
        ans = val in self.set_
        self.set_.add(val)
        return not ans

    def remove(self, val: int) -> bool:
        ans = val in self.set_
        if ans:
            self.set_.remove(val)
        return ans

    def getRandom(self) -> int:
        return random.choice(list(self.set_))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()