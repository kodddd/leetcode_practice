# solution1: 双指针
# 比起官方方法，可能多一次循环，因为无需保证元素总体一致，故无需交换，直接覆盖即可
# 时间复杂度 O(n)，空间复杂度 O(1)
class Solution(object):
    def jumpVal(self, nums, index, val):
        while index >= 0 and nums[index] == val:
            index -= 1
        return index

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tail = len(nums) - 1
        tail = self.jumpVal(nums, tail, val)
        i = 0
        while i < tail:
            if nums[i] == val:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail = self.jumpVal(nums, tail - 1, val)
            i += 1
        return tail + 1
