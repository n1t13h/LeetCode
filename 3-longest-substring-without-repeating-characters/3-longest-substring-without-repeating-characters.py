# Solution for 3. Longest Substring Without Repeating Characters
from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occurrence = {}
        max_length = 0
        left = 0
        for right in range(len(s)):
            current_char = s[right]
            if current_char in last_occurrence and last_occurrence[current_char] >= left:
                left = last_occurrence[current_char] + 1
            last_occurrence[current_char] = right
            current_length = right - left + 1
            max_length = max(max_length,current_length)
        return max_length
