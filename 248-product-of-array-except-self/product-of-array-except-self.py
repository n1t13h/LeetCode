from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Prefix multiplication
        pre = 1
        for i in range(n):
            result[i] = pre
            pre *= nums[i]

        # Postfix multiplication
        post = 1
        for i in range(n-1, -1, -1):
            result[i] *= post
            post *= nums[i]

        return result


# Time and Space Complexity:

#     Time Complexity: O(n)O(n) (single pass for prefix and postfix)
#     Space Complexity: O(1)O(1) (modifying the result array in-place)