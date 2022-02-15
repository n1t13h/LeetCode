from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbersDict = defaultdict(lambda:0)
        for i in range(len(nums)):
            numbersDict[nums[i]] += 1
        
        for i in range(len(nums)):
            if numbersDict[nums[i]] == 1:
                return nums[i]
        return -1