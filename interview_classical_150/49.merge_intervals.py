from typing import List


# 重点在于排序，知识点是排序的内置函数lambda写法
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for item in intervals:
            if item[0] <= merged[len(merged) - 1][1]:
                merged[len(merged) - 1][1] = max(merged[len(merged) - 1][1], item[1])
            else:
                merged.append(item)
        return merged


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
