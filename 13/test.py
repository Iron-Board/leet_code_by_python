"""單元測試

Test Command:
    ```
    python3 -m unittest test.py
    ```
"""

from unittest import TestCase
from main import Solution

class MainTest(TestCase):
    def test_main(self):
        sol = Solution()
        match = {
            'III': 3,
            'LVIII': 58,
            'MCMXCIV': 1994,
        }
        for k, v in match.items():
            self.assertEqual(sol.romanToInt(k), v)

