class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minheap = []

        for value, index in count.items():
            if len(minheap) < k:
                heapq.heappush(minheap, (index, value))
            else:
                heapq.heappushpop(minheap, (index, value))
        
        return[h[1] for h in minheap]
        
