class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        strList = [""] * numRows
        flag = False  # 代表往下遍历，True代表往上
        curLevel = 0
        for c in s:
            strList[curLevel] += c
            if curLevel == numRows - 1:
                flag = True
            elif curLevel == 0:
                flag = False
            if flag:
                curLevel -= 1
            else:
                curLevel += 1
        result = ""
        for item in strList:
            result += item
        return result
