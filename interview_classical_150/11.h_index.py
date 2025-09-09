# Solution 排序后遍历
# 时间复杂度O(nlogn)，空间复杂度O(1)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            if citations[i] > h:
                h += 1
            else:
                return h
        return h
