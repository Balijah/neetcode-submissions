class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        values = []

        for word in strs:
            sorted_letters = sorted(word)
            sorted_words = "".join(sorted_letters)
            res[sorted_words] = res.get(sorted_words, []) + [word]
        
        return [values for values in res.values()]