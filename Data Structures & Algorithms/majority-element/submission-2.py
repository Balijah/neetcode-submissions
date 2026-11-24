class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        majority = math.ceil(n / 2)

        hashmap = Counter(nums)

        for num in nums:
            if hashmap[num] >= majority:
                return num

