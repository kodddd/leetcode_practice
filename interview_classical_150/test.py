class Node:
    def __init__(self, x: int, next: "Node" = None):
        self.val = int(x)
        self.next = next


# 逆排序链表
class Solution:
    def reverseList(self, head: Node) -> Node:
        previous = None
        tmp = head
        while tmp != None:
            nextNode = tmp.next
            tmp.next = previous
            previous = tmp
            tmp = nextNode
        return previous

    def print_list(self, head: Node):
        while head != None:
            print(head.val)
            head = head.next


sol = Solution()
n = Node(1, Node(2, Node(3)))
sol.print_list(n)
sol.print_list(sol.reverseList(n))
