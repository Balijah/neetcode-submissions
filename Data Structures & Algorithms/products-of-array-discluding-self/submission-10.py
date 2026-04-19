class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            mul = 1
            j = i
            for j in range(len(nums)):
                if j != i:
                    mul *= nums[j]
            res.append(mul)
        return res        