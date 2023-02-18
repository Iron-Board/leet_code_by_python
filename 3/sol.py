class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = []
        len_max = 0
        for c in s:
            if c in substr:
                len_substr = len(substr)
                if len_substr > len_max:
                    len_max = len_substr
                substr = substr[substr.index(c)+1:]
                substr.append(c)
            else:
                substr.append(c)
        len_substr = len(substr)
        if len_substr > len_max:
            len_max = len_substr
        return len_max
