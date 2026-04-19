class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_elements = set(nums)
        res = 0
        for i in unique_elements:
            compare = i
            longest_subsequence = 1
            if (compare - 1) in unique_elements:
                continue
            while (compare + 1) in unique_elements:
                longest_subsequence += 1
                compare += 1
            res = max(longest_subsequence, res)
        
        return res
        