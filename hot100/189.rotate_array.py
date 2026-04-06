from typing import List


# 最初设想是将index的数移动到index+k，然后index=index+k，如此进行n次，但发现很多情况下这样不能覆盖所有的位置。
# 所以抵达末尾后不应当不断用取余来循环，而是当回到每次循环的初始点时，将该点+1
# 虽然时间复杂度还是o（n），但是比起翻转数组的解法还是太慢了
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = 0
        start = 0

        while count < n:
            # current指要rotate到新位置的当前位置
            current = start
            # 巧秒之处
            prev = nums[start]

            while True:
                next_idx = (current + k) % n
                # 灵活运用这个性质，把prev值填入位置时，顺道更新prev值
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if current == start:
                    break

            start += 1


l = [-1, -100, 3, 99]
Solution().rotate(l, 2)
print(l)
