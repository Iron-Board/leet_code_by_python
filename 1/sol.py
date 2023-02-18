from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for idx, value in enumerate(nums):
            diff = target - value
            if diff in diffs:
                return [diffs[diff], idx]
            diffs[value] = idx
