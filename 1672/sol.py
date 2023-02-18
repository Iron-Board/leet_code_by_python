from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for account in accounts:
            total = self._sum(account)
            if total > max:
                max = total
        return max

    def _sum(self, account: List[int]) -> int:
        total = 0
        for i in account:
            total += i
        return total
