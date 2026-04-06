from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 递归是一种优雅的可以反向遍历链表的方法
# 还可以采用转换为list双指针逼近
# 最节省空间的方法是翻转中间节点之后的链表，然后从头和中间分别遍历
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.frontPointer = head

        def recursively_check(currentNode=head):
            if currentNode == None:
                return True
            if not recursively_check(currentNode.next):
                return False
            if self.frontPointer.val != currentNode.val:
                return False
            self.frontPointer = self.frontPointer.next
            return True
