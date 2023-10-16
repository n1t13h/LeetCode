class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        
        r = 0
        count = 0
        while r < len(nums):
            if nums[r] == 1:
                count+=1
            else:
                count = 0
            if count > max_length:
                max_length = count
            r+=1
        return max_length