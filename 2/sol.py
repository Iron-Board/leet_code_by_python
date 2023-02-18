from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self._val = val
        self._next = next

    def __eq__(self, other: ListNode) -> bool:
        return self._val == other._val and self._next == other._next

    @property
    def val(self) -> int:
        return self._val

    @val.setter
    def val(self, val: int) -> None:
        self._val = val

    @property
    def next(self) -> Optional[ListNode]:
        return self._next

    @next.setter
    def next(self, next: Optional[ListNode]):
        self._next = next

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
        sum = []
        while True:
            sum.append(self._sum(l1, l2))
            l1, l2 = self._next(l1, l2)
            if l1 is None and l2 is None:
                break
        return ListNodes(self._carry(sum)).head  # 處理進位

    def _carry(self, sum: list[int]) -> list[int]:
        """處理進位"""
        _sum = []
        carry = 0
        for i in sum:
            s = i + carry
            r = s % 10 # 餘數
            carry = int(s / 10) # 商
            _sum.append(r)
        if carry > 0:
            _sum.append(carry)
        return _sum

    def _sum(self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[int]:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2.val
        if l2 is None:
            return l1.val
        return l1.val + l2.val

    def _next(self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> tuple[Optional[ListNode], Optional[ListNode]]:
        if l1 is None and l2 is None:
            return None, None
        if l1 is None:
            return None, l2.next
        if l2 is None:
            return l1.next, None
        return l1.next, l2.next
