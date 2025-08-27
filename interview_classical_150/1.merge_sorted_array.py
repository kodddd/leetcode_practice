# solution1
# 将 nums2 直接复制到 nums1 的后半部分，然后对 nums1 进行排序
# 时间复杂度 O((m+n)log(m+n))，空间复杂度 O(log(m+n))（排序所需的栈空间）
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()


# solution2
# 可以利用到 nums1 和 nums2 已经排序好的性质
# 从后向前遍历，比较 nums1 和 nums2 的元素，将较大的元素放到 nums1 的末尾
# 时间复杂度 O(m+n)，空间复杂度 O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        tail = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[tail] = nums2[p2]
                p2 -= 1
            else:
                nums1[tail] = nums1[p1]
                p1 -= 1
            tail -= 1
        if p2 >= 0:
            nums1[: tail + 1] = nums2[: p2 + 1]
