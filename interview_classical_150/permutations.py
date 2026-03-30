from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index: int):
            if index == len(nums):
                result.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[i], nums[index] = (
                    nums[index],
                    nums[i],
                )  # 把所有剩下可能的数字填到index的位置
                backtrack(index + 1)
                nums[i], nums[index] = (
                    nums[index],
                    nums[i],
                )

        result = []
        backtrack(0)
        return result
