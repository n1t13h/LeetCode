# Solution for 424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        maxf = 0
        max_length = 0
        count = {}

        for right in range(n):
            count[s[right]] = 1 + count.get(s[right],0)
            maxf = max(count[s[right]],maxf)

            while (right - left + 1) - maxf > k:
                count[s[left]]-=1
                left+=1

            max_length = max(max_length, right-left+1)
        return max_length