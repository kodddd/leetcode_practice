# Solution 记录当前格子的最大跳跃能力
# 关于能否抵到最后一个格子，本质上就是能否渡过所有的0格子，所以在0格子时只需判断当前的最大跳跃能力是否大于0
# 时间复杂度O(n)，空间复杂度O(1)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxStep = 0
        for i in range(len(nums) - 1):
            maxStep -= 1
            if nums[i] == 0:
                if maxStep > 0:
                    continue
                else:
                    return False
            if nums[i] > maxStep:
                maxStep = nums[i]
        return True
