class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            i = (left + right) // 2
            if nums[i] < target:
                left += 1
            elif nums[i] > target:
                right -= 1
            else:
                return i
        return -1 
