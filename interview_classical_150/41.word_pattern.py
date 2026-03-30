class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split(" ")
        dic1 = {}
        dic2 = {}
        if len(pattern) != len(sList):
            return False
        for i in range(len(pattern)):
            if sList[i] not in dic1:
                dic1[sList[i]] = pattern[i]
            else:
                if dic1[sList[i]] != pattern[i]:
                    return False
            if pattern[i] not in dic2:
                dic2[pattern[i]] = sList[i]
            else:
                if dic2[pattern[i]] != sList[i]:
                    return False
        return True


print(Solution().wordPattern("abba", "dog cat cat dog"))
print(Solution().wordPattern("abba", "dog cat cat fish"))
print(Solution().wordPattern("aaaa", "dog cat cat dog"))
