class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for c in magazine:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        for c in ransomNote:
            if c not in dic or dic[c] == 0:
                return False
            else:
                dic[c] -= 1
        return True


print(Solution().canConstruct("a", "b"))
print(Solution().canConstruct("aa", "ab"))
print(Solution().canConstruct("aa", "aab"))
