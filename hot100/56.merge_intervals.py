from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        result = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev_end:
                prev_end = max(prev_end, intervals[i][1])
            else:
                result.append([prev_start, prev_end])
                prev_start = intervals[i][0]
                prev_end = intervals[i][1]
        result.append([prev_start, prev_end])
        return result


print(Solution().merge([[4, 7], [1, 4]]))
