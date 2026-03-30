from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        queue = deque()
        self.preOrder(root, queue)
        last = None
        while len(queue) != 0:
            curNode = queue.popleft()
            if last != None:
                last.right = curNode
                last.left = None
            last = curNode

    def preOrder(self, root: Optional[TreeNode], queue) -> None:
        if root == None:
            return None
        queue.append(root)
        self.preOrder(root.left)
        self.preOrder(root.right)
