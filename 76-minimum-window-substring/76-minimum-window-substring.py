class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count_t = {}
        count_s = {}

        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        left = 0
        matched = 0
        min_length = float("inf")
        min_string = ""

        for right in range(len(s)):
            if s[right] in count_t:
                count_s[s[right]] = 1 + count_s.get(s[right], 0)

                if count_s[s[right]] == count_t[s[right]]:
                    matched += 1

                while matched == len(count_t):
                    window_size = right - left + 1
                    if window_size < min_length:
                        min_length = window_size
                        min_string = s[left:right + 1]

                    if s[left] in count_t:
                        count_s[s[left]] -= 1
                        if count_s[s[left]] < count_t[s[left]]:
                            matched -= 1
                    left += 1

        return min_string
