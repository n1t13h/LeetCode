# Solution for 567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        s2_count = {}

        left = 0
        if len(s1) > len(s2):
            return False

        for i in s1:
            s1_count[i] = 1 + s1_count.get(i, 0)

        for right in range(len(s2)):
            s2_count[s2[right]] = 1 + s2_count.get(s2[right], 0)

            window_size = right - left + 1
            if window_size == len(s1):
                if s1_count == s2_count:
                    return True

                s2_count[s2[left]] -= 1
                if s2_count[s2[left]] == 0:
                    del s2_count[s2[left]]

                left += 1

        return False
