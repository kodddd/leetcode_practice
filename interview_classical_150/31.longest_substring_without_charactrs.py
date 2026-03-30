# 时间复杂度：O(n)，其中 n 是字符串 s 的长度。每个字符被访问两次，第一次是 end 指针向右移动时，第二次是 start 指针向右移动时。
# 空间复杂度：O(min(m, n))，其中 m 是字符集的大小，n 是字符串 s 的长度。最坏情况下，字符串 s 中的所有字符都是不同的，因此需要 O(n) 的空间来存储窗口中的字符。对于 ASCII 字符串，字符集大小为 128，因此空间复杂度为 O(min(128, n))。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        maxLength = 0
        currentLength = 0
        dic = {}
        while start <= end and end < len(s):
            if s[end] not in dic or dic[s[end]] < start:
                currentLength += 1
                maxLength = max(currentLength, maxLength)
                dic[s[end]] = end
            else:
                start = dic[s[end]] + 1
                dic[s[end]] = end
                currentLength = end - start + 1
            end += 1
        return max(currentLength, maxLength)


print(Solution().lengthOfLongestSubstring("abcabcbb"))
