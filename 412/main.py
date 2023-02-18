from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [self._cal(i+1) for i in range(n)]

    def _cal(self, n: int) -> str:
        r3, r5 = n%3, n%5
        if r3 == 0 and r5 == 0:
            return "FizzBuzz"
        elif r3 == 0:
            return "Fizz"
        elif r5 == 0:
            return "Buzz"
        return str(n)
