class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        hashmap = {}
        total_words = len(strs)

        for word in strs:
            prefix = ''
            for letter in word:
                prefix += letter
                hashmap[prefix] = hashmap.get(prefix, 0) + 1
        
        longest = ""
        for prefix, count in hashmap.items():
            if count == total_words and len(prefix) > len(longest):
                longest = prefix
        
        return longest
