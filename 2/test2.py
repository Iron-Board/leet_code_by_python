"""單元測試

Test Command:
    ```
    python3 -m unittest 2/test2.py
    ```
"""

from unittest import TestCase
from .sol2 import Solution
from .sol2 import ListNodes

class MainTest(TestCase):
    def test_main(self):
        sol = Solution()
        cases = (
            (
                ListNodes([2,4,3]).head,
                ListNodes([5,6,4]).head,
                ListNodes([7,0,8]).head
            ),
            (
                ListNodes([0]).head,
                ListNodes([0]).head,
                ListNodes([0]).head
            ),
            (
                ListNodes([9,9,9,9,9,9,9]).head,
                ListNodes([9,9,9,9]).head,
                ListNodes([8,9,9,9,0,0,0,1]).head
            ),
        )
        for case in cases:
            self.assertEqual(sol.addTwoNumbers(case[0], case[1]), case[2])
