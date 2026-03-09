class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split()
        result = ""
        for item in strs:
            result = item.strip() + " " + result
        return result.strip()


print(Solution().reverseWords("a good  example"))
