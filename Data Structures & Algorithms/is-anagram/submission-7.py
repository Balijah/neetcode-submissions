class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        onehashmap = {}

        for i in s:
            onehashmap[i] = 1 + onehashmap.get(i, 0)
        
        for j in t:
            onehashmap[j] = onehashmap.get(j, 0) - 1

        for value in onehashmap.values():
            if value != 0:
                return False
        return True