class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            while i < j and s[i].isalnum() != True:
                i += 1
            while i < j and s[j].isalnum() != True:
                j -= 1
            if self.equalToIgnoringCase(s[i], s[j]):
                i += 1
                j -= 1
            else:
                return False
        return True

    def equalToIgnoringCase(self, a: str, b: str) -> bool:
        return a.lower() == b.lower()
