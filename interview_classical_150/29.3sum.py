from typing import List


class Solution:
    def threes(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break
            if (i - 1) >= 0 and nums[i - 1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    # 由于有序性
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                # 由于有序性
                elif s < 0:
                    l += 1
                elif s > 0:
                    r -= 1

        return result


print(Solution().threes([-1, 0, 1, 2, -1, -4]))
