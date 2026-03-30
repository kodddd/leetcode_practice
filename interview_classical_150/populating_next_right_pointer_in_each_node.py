from collections import deque


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# 层序遍历
class Solution:
    def connect(self, root: "Node") -> "Node":
        if root == None:
            return None
        queue = deque([root])
        while len(queue) != 0:
            n = len(queue)
            last = None
            for _ in range(n):
                curNode = queue.popleft()
                if last != None:
                    last.next = curNode
                if curNode.left != None:
                    queue.append(curNode.left)
                if curNode.right != None:
                    queue.append(curNode.right)
                last = curNode
        return root
