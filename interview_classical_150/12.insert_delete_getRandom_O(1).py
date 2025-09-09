# Solution: 变长数组+哈希表
# 时间复杂度O(1)，空间复杂度O(n)
# 1. 用哈希表存储元素及其在数组中的索引，用数组存储元素
# 2. 插入时，先检查哈希表中是否存在该元素，若不存在则插入到数组末尾，并在哈希表中记录其索引
# 3. 删除时，先检查哈希表中是否存在该元素，若存在则将该元素与数组末尾元素交换，并更新哈希表中末尾元素的索引，最后删除数组末尾元素和哈希表中的该元素
# 4. 获取随机元素时，直接从数组中随机选择一个元素返回
from random import choice


class RandomizedSet(object):
    def __init__(self):
        self.indices = {}
        self.nums = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.indices:
            return False
        id = self.indices[val]
        self.nums[id] = self.nums[-1]
        self.indices[self.nums[id]] = id
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
