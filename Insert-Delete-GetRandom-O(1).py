class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.hashmap = {}

        

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.nums.append(val)
        self.hashmap[val] = len(self.nums) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            index = self.hashmap[val]
            last = self.nums[-1]
            self.nums[index] = last
            self.nums.pop()

            self.hashmap[last] = index 
            del self.hashmap[val]
            return True
        else:
            return False

        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()