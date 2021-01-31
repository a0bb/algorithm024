from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return -1

        p, q = 0, 1
        while q < len(nums):
            if nums[p] != nums[q]:
                nums[p + 1] = nums[q]
                p += 1
            q += 1
        return p + 1


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return -1

        tail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1


if __name__ == '__main__':
    n = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s = Solution()
    _p = s.removeDuplicates(n)
    print(_p)
