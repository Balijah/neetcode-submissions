class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            sorted_strings = "".join(sorted(string))

            if sorted_strings in hashmap:
                hashmap[sorted_strings].append(string)
            else:
                hashmap[sorted_strings] = [string]

        return(list(hashmap.values()))