class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_of_elements = sum(nums)
        n = len(nums)
        actual_sum = (n * ( n + 1 ) ) / 2
        return int(actual_sum - sum_of_elements)