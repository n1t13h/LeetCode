import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        heap = []
        for num, freq in freq.items():
            heapq.heappush(heap, (freq,num))

        most_freq = heapq.nlargest(k, heap)

        result = [num for freq, num in most_freq]
        return result


