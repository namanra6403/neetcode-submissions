class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            temp = "".join(sorted(s))
            if temp in hmap:
                hmap[temp].append(s)
            else:
                hmap[temp] = [s]

        return list(hmap.values())