class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i]=1
        
        for j in t:
            if j not in hashmap or hashmap[j]==0:
                return False
            else:
                hashmap[j]-=1
        
        return True