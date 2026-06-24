class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            i = (left + right) // 2
            n = nums[i]
            if target > n:
                left = i + 1
            elif target < n:
                right = i - 1
            else:
                return i
        return -1