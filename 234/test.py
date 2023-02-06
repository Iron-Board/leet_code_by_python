"""單元測試

Test Command:
    ```
    python3 -m unittest test.py
    ```
"""

from unittest import TestCase
from main import ListNodes
from main import Solution

class TestMain(TestCase):
    def test_main(self) -> None:
        cases = {
            (ListNodes([1,2,2,1]).head, True),
            (ListNodes([1,2]).head, False),
            (ListNodes([1]).head, True),
            (ListNodes([1,2,1]).head, True)
        }
        sol = Solution()
        for case in cases:
            self.assertEqual(sol.isPalindrome(case[0]), case[1])
