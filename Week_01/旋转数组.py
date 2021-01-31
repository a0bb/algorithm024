from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return

        k, end = k % len(nums), len(nums) - 1
        # 反转前n-k个数据
        self.reverse(nums, 0, end - k)
        # 反转剩余数据
        self.reverse(nums, end - k + 1, end)
        # 全部翻转
        self.reverse(nums, 0, end)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return

        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    s.rotate(nums, k)
    print(nums)
