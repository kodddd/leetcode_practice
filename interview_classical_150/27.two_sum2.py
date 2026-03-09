from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, 1  # i为左边index，j为右边index
        while numbers[i] * 2 <= target and j < len(numbers):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif (
                numbers[i] + numbers[j]
                > target  # 非递减数列，j增长下去之后的和只会更大，跳过该i情况
                or numbers[i] + numbers[len(numbers) - 1]
                < target  # 该i前提下的最大可能和仍然小于target，跳过该i
                or (
                    i > 0 and numbers[i] == numbers[i - 1]
                )  # 当前i与之前i位置数值相等，在过去已经遍历过后续可能，未找到，直接跳过
            ):
                i += 1
                j = i + 1
            else:
                j += 1


# 原始解法在某些情况下会有重复计算，下面是优化版本，时间复杂度O(n)，空间复杂度O(1)，即缩减空间法，考虑一个n*n的矩阵空间，横纵坐标为i，j，上半三角形区域即为待搜索区域。
# 可以通过判断大小不断削减某一行/列，直至找到正确解
# 原始做法中的某一判断numbers[i] + numbers[len(numbers) - 1]，相当于该算法下的缩减行空间，但还有缩减列空间的优化方向没有考虑
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return []


solution = Solution()
print(solution.twoSum([3, 24, 50, 79, 88, 150, 345], 200))
