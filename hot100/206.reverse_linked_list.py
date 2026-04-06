# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_node = head
        cur_head = None
        while next_node != None:
            tmp = next_node.next
            next_node.next = cur_head
            cur_head = next_node
            next_node = tmp
        return cur_head
