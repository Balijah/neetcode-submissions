class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n):
            mul = 1
            for j in range(n):
                if i != j:
                    mul *= nums[j]
            res.append(mul)
        return res
