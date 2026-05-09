class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        nums = {}

        for index, element in enumerate(numbers):
            nums[element] = index + 1
        
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in nums:
                return [i + 1, nums[diff]]