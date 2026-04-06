# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 双指针法
# 利用了对于两段长度不等的链，可以考虑遍历完一条从另一条头再开始
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        ptrA = headA
        ptrB = headB
        while True:
            if ptrA == None and ptrB == None:
                return None
            if ptrA == ptrB:
                return ptrA
            if ptrA == None:
                ptrA = headB
            else:
                ptrA = ptrA.next
            if ptrB == None:
                ptrB = headA
            else:
                ptrB = ptrB.next
