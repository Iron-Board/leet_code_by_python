"""單元測試

Test Command:
    ```
    python3 -m unittest 1342/test.py
    ```
"""

from unittest import TestCase
from .sol import Solution

class TestMain(TestCase):
    def test_main(self):
        sol = Solution()
        cases = (
            ([[1,2,3],[3,2,1]], 6),
            ([[1,5],[7,3],[3,5]], 10),
            ([[2,8,7],[7,1,3],[1,9,5]], 17),
        )
        for case in cases:
            self.assertEqual(sol.maximumWealth(case[0]), case[1])
