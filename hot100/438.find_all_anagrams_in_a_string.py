from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        result = []
        if s_len < p_len:
            return []
        # 天才的地方是考虑到了字符只有26个小写英文字母的条件，我之前考虑过用list来存储，然后每次比较sorted之后的结果（类似另一道异位词的做法）但是太耗时了
        # 用数组的好处是不需要每次重新排序了，顺序已经是定好了
        # 需要记的知识点是ord函数求ascii值，以及97是a的ascii值
        s_count = [0] * 26
        p_count = [0] * 26
        # 构造初始p_count和s_count
        for i in range(p_len):
            p_count[ord(p[i]) - 97] += 1
            s_count[ord(s[i]) - 97] += 1
        if p_count == s_count:
            result.append(0)
        # 滑动窗口
        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1
            if s_count == p_count:
                result.append(i + 1)
        return result


print(Solution().findAnagrams("cbaebabacd", "abc"))
