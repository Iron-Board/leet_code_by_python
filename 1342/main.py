class Solution:
    def numberOfSteps(self, num: int) -> int:
        turns = 0
        while num != 0:
            num = self._reduce(num)
            turns += 1
        return turns

    def _reduce(self, num: int) -> int:
        """on step to reduce it to zero.

        In one step, if the current number is even, you have to divide it by `2`, otherwise, you have to subtract 1 from it.
        """
        if num % 2 == 0:
            return int(num / 2)
        return num - 1
