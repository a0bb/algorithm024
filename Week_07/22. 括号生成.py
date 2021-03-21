from typing import List


"""
1. 递归终止条件：左边括号数量和右边括号的数量都等于n
2. 剪枝
    1. 添加"("的条件："("数量小于n，则可以添加；
    2. 添加")"的条件：")"数量小于"("，则可以添加
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = set()
        self._generate(left=0, right=0, n=n, s='', result=result)
        return list(result)

    def _generate(self, left, right, n, s, result):
        if left == n and right == n:
            result.add(s)
            return

        if left < n:
            self._generate(left + 1, right, n, s + '(', result)
        if right < left:
            self._generate(left, right + 1, n, s + ')', result)
