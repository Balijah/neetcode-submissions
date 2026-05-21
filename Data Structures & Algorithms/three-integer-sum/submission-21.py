class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums_sorted = sorted(nums)

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
        
            while left < right:
                if nums_sorted[left] + nums_sorted[right] < -nums_sorted[i]:
                    left += 1
                elif nums_sorted[left] + nums_sorted[right] > -nums_sorted[i]:
                    right -= 1
                else:
                    res.add(tuple([nums_sorted[i], nums_sorted[left], nums_sorted[right]]))
                    left += 1
                    right -= 1
                    
        return list(res)

