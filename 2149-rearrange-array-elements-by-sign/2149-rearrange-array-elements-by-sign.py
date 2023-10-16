class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives = []
        positives = []
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        merged = []    
        for j in range(len(negatives)):
            merged.append(positives[j])
            merged.append(negatives[j])
        return merged