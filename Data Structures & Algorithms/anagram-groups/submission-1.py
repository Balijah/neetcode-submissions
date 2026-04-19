class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dedict = defaultdict(list)

        for i in strs:
            sorted_characters = sorted(i)
            sorted_words = "".join(sorted_characters)
            dedict[sorted_words].append(i)
        return list(dedict.values())