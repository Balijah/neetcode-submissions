class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, number in enumerate(nums):
            hashmap[number] = index

        for index, number in enumerate(nums):
            desired = target - number
            if desired in hashmap and hashmap[desired] != index:
                return [index, hashmap[desired]]