
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        
        for num in nums:
            if num == 1:
                count += 1
                max_length = max(max_length, count)
            else:
                count = 0

        return max_length
