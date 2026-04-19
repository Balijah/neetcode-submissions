class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssorted = sorted(s)
        tsorted = sorted(t)

        return ssorted == tsorted
        