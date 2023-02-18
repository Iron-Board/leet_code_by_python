"""FIXME: This may not work properly on the machine specified by the question ("we are dealing with an environment which could only store integers within the 32-bit signed integer"). Because in such environment, if the reversed integer overflows, you will not be able to get the correct value (well, because it overflowed before you can get it), then the overflowed value would be returned. So, I believe the checking of overflow should be performed before calculating the reversed integer.
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        #is_negative = bool(x < 0)
        #x = -x if x < 0 else x
        s = str(x)[::-1]
        pos_start = None
        for i in range(len(s)):
            if s[i] == 0:
                pos_start = i+1
            else:
                break
        s2 = f'-{s[pos_start:-1]}' if s[-1] == '-' else s[pos_start:]
        i = int(s2)
        return i if -(2**31) <= i <= 2**31 -1 else 0
