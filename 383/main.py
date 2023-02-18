class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = self._count_letters(ransomNote)
        d2 = self._count_letters(magazine)
        for k, v in d1.items():
            if k not in d2 or v > d2[k]:
                return False
        return True

    def _count_letters(self, s: str) -> dict:
        letters = {}
        for char in s:
            letters[char] = letters.get(char, 0) + 1
        return letters
