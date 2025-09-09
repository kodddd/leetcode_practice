# Solution: 前缀积和后缀积
# 时间复杂度O(n)，空间复杂度O(n)
# 1. 用两个数组分别存储每个元素左侧所有元素的乘积和右侧所有元素的乘积
# 2. 最后将两个数组对应位置的元素相乘即为结果
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)
        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
            right[len(nums) - 1 - i] = right[len(nums) - i] * nums[len(nums) - i]
        for i in range(0, len(nums)):
            if i == 0:
                answer[i] = right[i]
            elif i == len(nums) - 1:
                answer[i] = left[i]
            else:
                answer[i] = left[i] * right[i]
        return answer
