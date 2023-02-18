"""單元測試

Test Command:
    ```
    python3 -m unittest 1342/test.py
    ```
"""

from unittest import TestCase
from .main import Solution

class TestMain(TestCase):
    def test_main(self):
        sol = Solution()
        cases = (
            (14, 6),
            (8, 4),
            (123, 12),
        )
        for case in cases:
            self.assertEqual(sol.numberOfSteps(case[0]), case[1])

