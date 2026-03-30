# 这一个版本是对两数之和的拙劣模仿，耗时会多一些，虽然代码简单点
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            # 已经是排序后了，如果第一个数大于0，后续不可能和别的数加起来等于0，剪枝
            if nums[i] > 0:
                break
            # 避免第一个数的重复情况
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            dic = {}
            for j in range(i + 1, len(nums)):
                if nums[j] not in dic:
                    # key为未来出现的数的期望值，值为是否用到过，避免重复计入
                    dic[-nums[i] - nums[j]] = False
                elif nums[j] in dic and not dic[nums[j]]:
                    result.append([nums[i], -nums[j] - nums[i], nums[j]])
                    dic[nums[j]] = True
        return result


print(Solution().threeSum([0, 0, 0, 0]))
