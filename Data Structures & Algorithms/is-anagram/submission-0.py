class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sletters = list(s)
        tletters = list(t)
        sletters.sort()
        tletters.sort()
        if sletters == tletters:
            return True
        return False