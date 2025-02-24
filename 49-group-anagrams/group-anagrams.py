from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            sorted_key = "".join(sorted(s))
            hashmap[sorted_key].append(s)
        return list(hashmap.values())
