"""單元測試

Test Command:
    ```
    python3 -m unittest 383/test.py
    ```
"""

from unittest import TestCase
from .main import Solution

class TestMain(TestCase):
    def test_main(self) -> None:
        cases = (
            ('a', 'b', False),
            ('aa', 'ab', False),
            ('aa', 'aab', True),
        )
        sol = Solution()
        for case in cases:
            self.assertEqual(sol.canConstruct(case[0], case[1]), case[2])
