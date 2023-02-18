"""單元測試

Test Command:
    ```
    python3 -m unittest 4/test2.py
    ```
"""

from unittest import TestCase
from .sol2 import Solution

class MainTest(TestCase):
    def test_main(self):
        sol = Solution()
        cases = (
            ([1,3], [2], 2.0),
            ([1,2], [3,4], 2.5),
        )
        for case in cases:
            self.assertEqual(sol.findMedianSortedArrays(case[0], case[1]),
                             case[2])
