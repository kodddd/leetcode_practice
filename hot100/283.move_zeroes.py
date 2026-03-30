from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        # 快慢指针，right找非0，交换位置
        # 满足性质：left左边皆非0，left至right皆为0，left本身指向是否为0不确定
        while right < len(nums):
            if nums[right] == 0:
                right += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
print(nums)
