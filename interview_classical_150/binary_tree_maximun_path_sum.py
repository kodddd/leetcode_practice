# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    maxTotal = -math.inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxGain(root)
        return self.maxTotal

    def maxGain(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        maxLeft = self.maxGain(root.left)
        maxRight = self.maxGain(root.right)
        self.maxTotal = max(self.maxTotal, root.val + maxLeft + maxRight)
        returnVal = root.val + max(maxLeft, maxRight)
        if returnVal > 0:
            return returnVal
        else:
            return 0
