class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            sorted_letters = sorted(i)
            sorted_words = ''.join(sorted_letters)
            res[sorted_words] = res.get(sorted_words, []) + [i]    
        
        return[values for values in res.values()]