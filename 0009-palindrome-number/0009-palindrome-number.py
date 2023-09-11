class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        while (x > 0):
            ld = x % 10
            rev = rev * 10 + ld
            x = x // 10
        return True if temp == rev else False
