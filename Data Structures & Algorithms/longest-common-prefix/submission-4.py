class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Initialize answer
        res = ""

        # Use first string as a character reference
        for i in range(len(strs[0])):
            # Loop through the same index for all strings
            for s in strs:
                # At the end of the current string OR a mismatch occurs
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        
        return res