"""單元測試

Test Command:
    ```
    python3 -m unittest 1337/test.py
    ```
"""

from unittest import TestCase
from .main import Solution

class TestMain(TestCase):
    def test_main(self):
        sol = Solution()
        cases = (
            (
                [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3,
                [2,0,3]
            ),
            (
                [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]],
                2,
                [0,2]
            )
        )
        for case in cases:
            self.assertEqual(sol.kWeakestRows(case[0], case[1]), case[2])
