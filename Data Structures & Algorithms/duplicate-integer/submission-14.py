class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = Counter(nums)

        for count in duplicates.values():
            if count > 1:
                return True
        
        return False
        