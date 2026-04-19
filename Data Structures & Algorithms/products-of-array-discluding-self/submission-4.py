class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for index, value in enumerate(nums):
            mul = 1
            for i, v in enumerate(nums):
                if index != i:
                    mul *= v
            res.append(mul)
        return res