# solution: 哈希表
# 使用变量存储必要信息，避免最后遍历哈希表找出majority element
# 但这是更广泛的解法，可以找到出现次数最多的数，并没有有效利用到“存在一个数的出现次数大于⌊ n/2 ⌋”这个条件
# 时间复杂度O(n), 空间复杂度O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = 0
        maxNum = 0
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            if maxCount < d[num]:
                maxCount = d[num]
                maxNum = num
        return maxNum


# solution 2: Boyer-Moore投票算法
# 利用“存在一个数的出现次数大于⌊ n/2 ⌋”这个条件
# 类似于消去法，抵消掉不同的数，最后剩下的数即为majority element
# count+-可以理解为入场和离场的人数，majority element的入场人数多于离场人数，最后剩下的就是majority element
# 时间复杂度O(n), 空间复杂度O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
