class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []

        left = 0
        for right in range(len(nums)):
            size = right - left + 1
            if size == k:
                results.append(max(nums[left:right+1]))
                left+=1

        return results