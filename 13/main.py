class Solution:

    _dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }

    def romanToInt(self, s: str) -> int:
        j = 0
        sum = 0
        for i in range(len(s)):
            if i == j:
                add = self._dict.get(s[i:i+2])
                if add is not None:
                    sum += add
                    j = i+2
                else:
                    sum += self._dict.get(s[i:i+1])
                    j = i+1
        return sum
