from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNodes:
    def __init__(self, values: list[int]) -> None:
        node_next = None
        values.reverse()
        for value in values:
            node_next = ListNode(value, node_next)
        self._head = node_next

    @property
    def head(self) -> ListNode:
        return self._head

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head is not None:
            nodes.append(head)
            head = head.next
        mid = int(len(nodes)/2)
        return nodes[mid]
