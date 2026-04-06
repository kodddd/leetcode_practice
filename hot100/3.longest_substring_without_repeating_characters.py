class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        currentLength = 0
        maxLength = 0
        start = 0
        for i in range(len(s)):
            if s[i] not in dic or dic[s[i]] < start:
                currentLength += 1
                maxLength = max(maxLength, currentLength)
            else:
                currentLength = i - dic[s[i]]
                start = dic[s[i]] + 1
            dic[s[i]] = i
        return maxLength


print(Solution().lengthOfLongestSubstring("pwwkew"))
