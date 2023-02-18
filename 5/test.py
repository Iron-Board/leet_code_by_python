"""單元測試

Test Command:
    ```
    python3 -m unittest 5/test.py
    ```
"""

from unittest import TestCase
from .sol import Solution

class MainTest(TestCase):
    def test_main(self):
        sol = Solution()
        cases = (
            ('babad', ['bab', 'aba']),
            ('cbbd', ['bb']),
            ('aacabdkacaa', ['aca']),
            ('aaaa', ['aaaa'])
        )
        for case in cases:
            self.assertIn(sol.longestPalindrome(case[0]), case[1])
