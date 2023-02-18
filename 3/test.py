"""單元測試

Test Command:
    ```
    python3 -m unittest 3/test.py
    ```
"""

from unittest import TestCase
from .sol import Solution

class MainTest(TestCase):
    def test_main(self):
        sol = Solution()
        cases = (
            ('abcabcbb', 3),
            ('bbbbb', 1),
            ('pwwkew', 3),
            ('aab', 2),
            ('dvdf', 3)
        )
        for case in cases:
            self.assertEqual(sol.lengthOfLongestSubstring(case[0]), case[1])
