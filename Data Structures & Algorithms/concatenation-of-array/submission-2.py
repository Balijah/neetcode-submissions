class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [0] * (2 * n)

        left = 0
        right = n

        for i in range(n):
            ans[left] = nums[i]
            ans[right] = nums[i]
            left += 1
            right += 1
        
        return ans

        