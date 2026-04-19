class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefixarray = []
        postfixarray = []

        prefix = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            prefixarray.append(prefix)

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix *= nums[i]
            postfixarray.append(postfix)
        postfixarray.reverse()

        for i in range(len(nums)):
            if i == 0:
                res.append(postfixarray[1])
            elif i == (len(nums) - 1):
                res.append(prefixarray[len(nums) - 2])
            else:
                result = prefixarray[i - 1] * postfixarray[i + 1]
                res.append(result)
        return res



