class Solution:
    def minimumLength(self, s: str) -> int:
        l,r = 0 , len(s)-1
        previous = None
        if len(s) == 1:
            return 1
        while l <= r:
            if s[l] == s[r]:
                previous = s[l]
                l+=1
                r-=1
            elif previous == s[l]:
                l+=1
            elif previous == s[r]:
                r-=1
            else:
                return r-l+1
        return int(s[l] != previous)