from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 不能用滑动窗口，如果都是正整数的话可以，因为现在这样不知道该缩左边还是扩右边
        # 可以用一个类似dp的方法
        # 连续子串的和就是end的前缀和-start的前缀和，而从前往后遍历计算到end的前缀和的时候，start的前缀和已经得出了
        dic = {0: 1}
        prevSum = 0
        count = 0
        for num in nums:
            prevSum += num
            if prevSum - k in dic:
                count += dic[prevSum - k]
            if prevSum not in dic:
                dic[prevSum] = 1
            else:
                dic[prevSum] += 1
        return count


print(
    Solution().subarraySum(
        [1],
        0,
    )
)
