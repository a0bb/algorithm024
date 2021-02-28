from typing import List
import collections


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if k <= 0 or n < k:
            return res
        # path 栈
        path = collections.deque()
        self._dfs(n, k, 1, path, res)
        return res

    def _dfs(self, n, k, begin, path, res):
        if len(path) == k:
            if list(path) not in res:
                res.append(list(path))
            return

        for i in range(begin, n + 1):
            path.append(i)
            # print(f'递归前path: {path}')
            self._dfs(n, k, i + 1, path, res)
            path.pop()
            # print(f'递归后path: {path}')


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
