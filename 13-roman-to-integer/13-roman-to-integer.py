class Solution:
    def romanToInt(self, s: str) -> int:
        romandict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        total = 0
        for i in range(len(s)):
            if i > 0 and romandict[s[i]] > romandict[s[i-1]]:
                total += romandict[s[i]] - 2 * romandict[s[i-1]]
            else:
                total += romandict[s[i]]
        return total