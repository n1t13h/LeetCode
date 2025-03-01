# Solution for 239. Sliding Window Maximum
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        dq = deque()
        left = 0

        for right in range(len(nums)):
            if dq and dq[0] < left:
                x = dq.popleft()

            while dq and nums[dq[-1]] < nums[right]:
                y = dq.pop()

            dq.append(right)

            if right >= k - 1:
                results.append(nums[dq[0]])
                left += 1

        return results


solution = Solution()
print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]