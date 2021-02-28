from typing import List


"""
三种情况分别处理
[1]
[4, 5, 6, 7, 0, 1, 2]
[4, 7, 9]
O(n)
"""
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[0]


"""
二分查找
"""
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            elif nums[middle] < nums[right]:
                right = middle
        return nums[left]


if __name__ == '__main__':
    s = Solution2()
    _nums = [11, 13, 15, 17]
    print(s.findMin(_nums))