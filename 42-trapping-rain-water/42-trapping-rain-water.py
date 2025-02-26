# Solution for 42. Trapping Rain Water
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_max = height[left]
        right_max = height[right]
        res = 0
        while left < right:
            if left_max < right_max:
                left+=1
                left_max = max(left_max,height[left])
                res+= left_max - height[left]
            else:
                right -=1
                right_max = max(right_max,height[right])
                res += right_max - height[right]

        return res