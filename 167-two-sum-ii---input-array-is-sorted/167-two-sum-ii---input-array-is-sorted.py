# Solution for 167. Two Sum II - Input Array Is Sorted
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left , right = 0,len(numbers) - 1
        while left < right:
            summed = numbers[left]+ numbers[right]

            if summed == target:
                return [left+1,right+1]

            if summed > target:
                right -=1
            else:
                left +=1


        return []