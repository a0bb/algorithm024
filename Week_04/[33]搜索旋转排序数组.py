from typing import List


"""
概括：以中间点分割，然后在有序的一边查找；然后循环
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle

            if nums[left] <= nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    _nums = [4,5,6,7,0,1,2]
    _target = 0
    print(s.search(_nums, _target))


