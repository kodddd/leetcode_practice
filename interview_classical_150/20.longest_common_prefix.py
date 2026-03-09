from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        length = len(strs[0])
        count = len(strs)

        for i in range(length):
            c = strs[0][i]

            for j in range(1, count):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]

        return strs[0]


print(Solution().longestCommonPrefix(["a"]))
