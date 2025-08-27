import sys

# solution 1: 双指针，但是收到了2的影响，选择了左右双指针，解法不好
# 时间复杂度O(nlog(n)), 空间复杂度O(n)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        left = 0
        right = len(nums)
        while left < right:
            if nums[left] in s:
                nums[left] = nums[right - 1]
                nums[right - 1] = sys.maxint
                right -= 1
            else:
                s.add(nums[left])
                left += 1
        nums.sort()
        return left


# solution 2: 双指针，快慢指针
# 之所以可以不花空间存储，利用了数组是排序的这个条件
# 时间复杂度O(n), 空间复杂度O(1)


class Solution2(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
