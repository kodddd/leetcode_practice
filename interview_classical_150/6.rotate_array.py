## solution: 三次反转
# 利用了右移k位相当于将数组分为两部分，先整体反转，再分别反转两部分
# 时间复杂度O(n), 空间复杂度O(1)
class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[0 : len(nums)] = reversed(nums[0 : len(nums)])
        nums[0:k] = reversed(nums[0:k])
        nums[k : len(nums)] = reversed(nums[k : len(nums)])
