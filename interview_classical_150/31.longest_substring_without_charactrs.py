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
