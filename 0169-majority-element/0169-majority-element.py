

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int)
        
        majority_count = n // 2
        for num in nums:
            m[num] += 1
            if m[num] > majority_count:
                return num
        
        return 0
