import collections
from typing import List


# 一开始的想法比较草率，但问题是如果离开窗口的值正好是之前的最大值，那么我怎么找到第二大的值呢？如果是之前的第二大值，怎么更新为第三大的值呢？
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         maxIndex = 0
#         maxSecondIndex = 0
#         maxCount = -float("inf")
#         maxSecondCount = -float("inf")
#         # 构造最初的滑动窗口
#         for i in range(k):
#             if nums[i] > maxCount:
#                 maxSecondCount = maxCount
#                 maxSecondIndex = maxIndex
#                 maxCount = nums[i]
#                 maxIndex = i
#         for i in range(k,len(nums)):
#             if i-k==maxIndex:


# 但是有一个数据结构很好地解决了这个问题，即双向队列。它维持了从左到右一定是index对应value从大到小的特性，同时还保证了从左到右的index是以左边为先出现的
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            print(q)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
