from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        tmp = []
        currentLength = 0
        result = []
        for word in words:
            if currentLength + len(word) <= maxWidth:
                tmp.append(word)
                currentLength += len(word) + 1
                continue
            else:
                result.append(self.deal_with_tmp(tmp, maxWidth, False))
                currentLength = len(word) + 1
                tmp = [word]
        if len(tmp) > 0:
            result.append(self.deal_with_tmp(tmp, maxWidth, True))
        return result

    def deal_with_tmp(self, tmp: List[str], maxWidth: int, final: bool) -> str:
        totalBlank = maxWidth
        result = ""
        if final:
            for item in tmp:
                result = result + item
                if totalBlank > 0:
                    result += " "
                else:
                    return result
                totalBlank = totalBlank - len(item) - 1
            result += " " * totalBlank
            result = result[:maxWidth]
        else:
            for item in tmp:
                totalBlank -= len(item)
            blankNum = len(tmp) - 1
            if blankNum == 0:
                return tmp[0] + " " * totalBlank
            perBlank = totalBlank // blankNum
            left = totalBlank % blankNum
            for item in tmp:
                result = result + item + " " * perBlank
                if left > 0:
                    result += " "
                    left -= 1
            result = result[:maxWidth]
        return result


print(
    Solution().fullJustify(
        [
            "ask",
            "not",
            "what",
            "your",
            "country",
            "can",
            "do",
            "for",
            "you",
            "ask",
            "what",
            "you",
            "can",
            "do",
            "for",
            "your",
            "country",
        ],
        16,
    )
)
