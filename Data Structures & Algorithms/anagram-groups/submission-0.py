from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        newmap = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            newmap[sorted_s].append(s)
        
        results = newmap.values()
        return results