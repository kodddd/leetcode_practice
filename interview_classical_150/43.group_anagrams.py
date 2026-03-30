from typing import List


# 重点就在于找到字典的key，具有同一异位词相等的特性，而排序后的字符串可以满足这个特性
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dic = {}
        for item in strs:
            sortedItem = "".join(sorted(item))
            if sortedItem in dic:
                dic[sortedItem].append(item)
            else:
                dic[sortedItem] = [item]
        for item in dic:
            result.append(dic[item])
        return result


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
