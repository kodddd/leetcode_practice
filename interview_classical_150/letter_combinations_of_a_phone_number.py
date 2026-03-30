from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        collections = []

        def backTrack(index: int, path: str):
            if index == len(digits):
                collections.append(path)
                return
            for ch in phoneMap[digits[index]]:
                backTrack(index + 1, path + ch)

        if digits:
            backTrack(0, "")

        return collections
