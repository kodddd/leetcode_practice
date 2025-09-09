import sys


# Solution 记录到达每个格子的最小跳跃次数(较差的解法)
# 时间复杂度O(n^2)，空间复杂度O(n)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        for current in range(1, len(nums)):
            minStep = sys.maxint
            for i in range(current):
                if nums[i] + i >= current and dp[i] + 1 < minStep:
                    minStep = dp[i] + 1
            dp[current] = minStep
        return dp[len(nums) - 1]


# solution 贪心算法
# 记录当前能跳跃到的最远位置，以及上次跳跃能到达的最远位置
# 当遍历到上次跳跃能到达的最远位置时，更新跳跃次数，并将上次跳跃能到达的最远位置更新为当前能跳跃到的最远位置
# 有点类似于bfs的层次遍历
# 时间复杂度O(n)，空间复杂度O(1)
class Solution(object):
    def jump(self, nums):
        n = len(nums)
        # maxPos 在当前位置之前能跳跃到的最远位置
        # end 上次跳跃能到达的最远位置
        # step 跳跃次数
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if (
                maxPos >= i
            ):  # 表明当前位置能到达，但由于面试经典150保证了一定能到达最后一个位置，所以这里的if条件不强制要求
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
            print(maxPos, end, step)
        return step


# test
s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
