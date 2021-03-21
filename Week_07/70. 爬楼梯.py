from typing import List


# 记忆化搜索 + 剪枝
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * n
        return self._recursion(n, memo)

    def _recursion(self, n: int, memo: List[int]) -> int:
        if n <= 2:
            return n
        if memo[n - 1] == 0:
            memo[n - 1] = self._recursion(n - 1, memo) + self._recursion(n - 2, memo)
        return memo[n - 1]
