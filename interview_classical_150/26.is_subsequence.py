class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if i == len(s):
                break
            if s[i] == t[j]:
                i += 1
        if i == len(s):
            return True
        return False
