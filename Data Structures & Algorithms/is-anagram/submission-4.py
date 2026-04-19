class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}

        for i in s:
            smap[i] = 1 + smap.get(i, 0)
        
        for j in t:
            tmap[j] = 1 + tmap.get(j, 0)

        print(smap)
        print(tmap)
        
        return smap == tmap
        