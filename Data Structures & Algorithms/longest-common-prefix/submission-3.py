class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Start with first word as prefix
        prefix = strs[0]

        # Compare against every other word in the list
        for word in strs[1:]:
            # Chop off the last until the current word starts with "prefix"
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix