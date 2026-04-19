class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        heap = []

        for number, frequency in freq.items():
            if len(heap) != k:
                heapq.heappush(heap, (frequency, number))
            elif len(heap) == k:
                if (frequency, number) > heap[0]:
                    heapq.heappushpop(heap, (frequency, number))
        
        return [number for frequency, number in heap]