class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Check for potential overflow before reversing
        if x > INT_MAX or x < INT_MIN:
            return 0
        
        num = int(str(abs(x))[::-1])
        
        if num > INT_MAX:
            return 0
        
        if x < 0:
            return -num
        return num
