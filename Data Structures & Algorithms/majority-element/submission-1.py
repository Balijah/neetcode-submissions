class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        majority = math.ceil(n / 2)

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        
            if hashmap[num] >= majority:
                return num
