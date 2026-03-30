class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = t[i]
            else:
                if dic1[s[i]] != t[i]:
                    return False
            if t[i] not in dic2:
                dic2[t[i]] = s[i]
            else:
                if dic2[t[i]] != s[i]:
                    return False
        return True


print(Solution().isIsomorphic("badc", "baba"))
