# KMP算法，时间复杂度O(m+n)，空间复杂度O(n)，m和n分别是haystack和needle的长度
# 1. 构建next数组，记录needle中每个位置之前的最长相同前后缀的长度
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        next = self.build_next(needle)
        i=0 
        j = 0
        while i<len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = next[j-1]
            else:
                i += 1
            if j == len(needle):
                return i-j
        return -1

    def build_next(self, needle) -> list:
        next = [0]
        prefix_length = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[prefix_length]:
                prefix_length += 1
                next.append(prefix_length)
                i += 1
            elif prefix_length > 0:
                prefix_length = next[prefix_length - 1]
            else:
                next.append(0)
                i += 1
        return next


print(Solution().strStr("hello", "ll"))
