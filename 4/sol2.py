from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self._merge(nums1, nums2)
        # print(nums)
        size = len(nums)
        return (nums[int((size-1)/2)] + nums[int(size/2)] ) / 2

    def _merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        len_1 = len(nums1)
        len_2 = len(nums2)
        pos_1 = 0
        pos_2 = 0
        while pos_1 < len_1 or pos_2 < len_2:
            if pos_1 < len_1 and pos_2 < len_2:
                if nums1[pos_1] <= nums2[pos_2]:
                    nums.append(nums1[pos_1])
                    pos_1 += 1
                else:
                    nums.append(nums2[pos_2])
                    pos_2 += 1
            elif pos_1 < len_1:
                nums.append(nums1[pos_1])
                pos_1 += 1
            else:
                nums.append(nums2[pos_2])
                pos_2 += 1
        return nums
