class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a,b=0,0
        minimum = min(len(word1),len(word2))
        result = ""
        while(a < minimum or b < minimum):
            result += word1[a]
            result += word2[b]
            a+=1
            b+=1
        
        result += word2[minimum:len(word2)]
        result += word1[minimum:len(word1)]
        return result