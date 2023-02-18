from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        size = len(nums)
        return (nums[int((size-1)/2)] + nums[int(size/2)] ) / 2
