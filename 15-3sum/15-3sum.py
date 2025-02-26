# Solution for 15. 3Sum
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()
        results= []
        for i in range(0,n-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    results.append([nums[i],nums[left],nums[right]])

                    left +=1
                    right -=1

                    while left < right and nums[left] == nums[left-1]:
                        left+=1

                    while left < right and nums[right] == nums[right+1]:
                        right -=1

                elif total > 0:
                    right -=1
                else:
                    left+=1

        return results
