"""單元測試

Test Command:
    ```
    python3 -m unittest 412/test.py
    ```
"""

from unittest import TestCase
from .main import Solution

class TestMain(TestCase):
    def test_main(self) -> None:
        cases = (
            (3, ["1","2","Fizz"]),
            (5, ["1","2","Fizz","4","Buzz"]),
            (15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]),
        )
        sol = Solution()
        for case in cases:
            self.assertEqual(sol.fizzBuzz(case[0]), case[1])
