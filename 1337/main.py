from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = self._count_soldiers(mat)
        soldiers = sorted(soldiers.items(), key=lambda soldiers: soldiers[1])
        return [counts[0] for counts in soldiers][:k]

    def _count_soldiers(self, mat: List[List[int]]) -> dict:
        rsts = {}
        for idx, row in enumerate(mat):
            count = 0
            for item in row:
                if item == 1:
                    count += 1
            rsts[idx] = count
        return rsts
