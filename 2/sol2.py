from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other: ListNode) -> bool:
        return self.val == other.val and self.next == other.next

class ListNodes:
    def __init__(self, values: list[int]) -> None:
        node_next = None
        values.reverse()
        for value in values:
            if value is not None:
                node_next = ListNode(value, node_next)
        self._head = node_next

    @property
    def head(self) -> ListNode:
        return self._head

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head_pre = ListNode()
        node_pre = head_pre
        carry = 0  # 進位值
        while l1 or l2 or carry:
            val = carry  # 新 ListNode 值
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            # See: https://docs.python.org/3/library/functions.html#divmod
            carry, val = divmod(val, 10)
            node = ListNode(val)
            node_pre.next = node
            node_pre = node
        return head_pre.next
