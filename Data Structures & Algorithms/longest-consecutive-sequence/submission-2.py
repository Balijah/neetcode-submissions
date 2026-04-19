class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = set()
        for i in range(len(nums)):
            freq.add(nums[i])
        res = 0
        for i in range(len(nums)):
            current_length = 1
            current_number = nums[i]

            while (current_number + 1) in freq:
                current_number += 1
                current_length += 1
            
            res = max(res, current_length)
        return res