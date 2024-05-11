import itertools
from typing import List
import heapq


def mincostToHireWorkers(quality: List[int], wage: List[int], k: int) -> float:
    res = float('inf')
    pairs = [(w/q, q) for w, q in zip(wage, quality)]
    pairs.sort(key=lambda x: x[0])

    max_heap = []
    total_quality = 0
    for ratio, q in pairs:
        heapq.heappush(max_heap, -q)
        total_quality += q
        if len(max_heap) > k:
            total_quality += heapq.heappop(max_heap)
        if len(max_heap) == k:
            res = min(res, total_quality * ratio)

    return res


quality = [3, 1, 10, 10, 1]
wages = [4, 8, 2, 2, 7]

k = 3
print(mincostToHireWorkers(quality, wages, k))
