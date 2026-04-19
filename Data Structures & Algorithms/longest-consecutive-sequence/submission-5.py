class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_elements = set(nums)
        res = 0
        for i in range(len(nums)):
            compare = nums[i]
            longest_seq = 1
            if (nums[i] - 1) in unique_elements:
                continue
            while (compare + 1) in unique_elements:
                longest_seq += 1
                compare += 1
            res = max(longest_seq, res)
        
        return res
        