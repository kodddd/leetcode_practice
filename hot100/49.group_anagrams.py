from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dic = {}
        for str in strs:
            sortedStr = "".join(sorted(str))
            if sortedStr in dic:
                dic[sortedStr].append(str)
            else:
                dic[sortedStr] = [str]
        for l in dic:
            result.append(dic[l])
        return result


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
