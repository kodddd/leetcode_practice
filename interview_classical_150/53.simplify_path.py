class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split("/"):
            if item == "." or len(item) == 0:
                continue
            elif item == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(item)
        return "/" + "/".join(stack)


print(Solution().simplifyPath("/.../a/../b/c/../d/./"))
