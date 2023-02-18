"""單元測試

Test Command:
    ```
    python3 -m unittest 876/test.py
    ```
"""

from unittest import TestCase
from .main import Solution
from .main import ListNode
from .main import ListNodes

class TestMain(TestCase):
    def test_main(self):
        sol = Solution()
        cases = (
            ([1, 2, 3, 4, 5], 3),
            ([1, 2, 3, 4, 5, 6], 4)
        )
        for case in cases:
            mid = sol.middleNode(ListNodes(case[0]).head)
            self.assertIsInstance(mid, ListNode)
            self.assertEqual(mid.val, case[1])
