class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 # initial starting point
        right = len(nums) - 1 # initial ending point

        while left <= right: # while left is less than OR EQUAL TO the right pointer
            mid = (left + right) // 2 # split the array in half using integer division
            if nums[mid] < target: # if the middle value is LESS than the target, we can eliminate the whole half by incrementing left by 1
                left = mid + 1
            elif nums[mid] > target: # if the middle value is GREATER than the target, we can eliminate the whole half by decrementing right by 1
                right = mid - 1
            else:
                return mid # If mid is not larger or less than the target then it must be EQUAL TO (hence the 'while left <= right)
        return -1
