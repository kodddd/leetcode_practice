## solution: 双指针，快慢指针
## 和初级版区别仅在于用了一个bool值存储是否当前数字已经出现过两次，同样利用了数组是排序的这个条件
## 时间复杂度O(n), 空间复杂度O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        over_two = False
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
                over_two = False
            else:
                if not over_two:
                    over_two = True
                    nums[slow] = nums[fast]
                    slow += 1
            fast += 1
        return slow
