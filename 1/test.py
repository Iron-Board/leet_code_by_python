"""單元測試

Test Command:
    ```
    python3 -m unittest 1/test.py
    ```
"""

from unittest import TestCase
from .sol import Solution

class MainTest(TestCase):
    def test_main(self):
        sol = Solution()
        cases = (
            ([2,7,11,15], 9, [0, 1]),
            ([3,2,4], 6, [1,2]),
            ([3,3], 6, [0,1])
        )
        for case in cases:
            self.assertEqual(sol.twoSum(case[0], case[1]), case[2])
