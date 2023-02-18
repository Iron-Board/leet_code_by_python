"""單元測試

Test Command:
    ```
    python3 -m unittest 7/test.py
    ```
"""

from unittest import TestCase
from .sol import Solution
from .cases import cases

class MainTest(TestCase):
    def test_main(self):
        sol = Solution()
        for case in cases:
            self.assertEqual(sol.reverse(case[0]), case[1])
