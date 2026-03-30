from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        return None

    def reverse(self, head: Optional[ListNode]):
        curNode = head
        prevNode = None
        while curNode != None:
            tmp = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = tmp

        return prevNode
