class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        

        for c, n in count.items():      # c = key(frequency)
            freq[n].append(c)           # n = value(number)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for z in freq[i]:
                res.append(z)
                if len(res) == k:
                    return res