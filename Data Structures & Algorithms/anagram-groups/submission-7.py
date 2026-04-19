class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            sorted_letters = sorted(i)
            sorted_words = ''.join(sorted_letters)
            res[sorted_words].append(i)  
        
        return(list(res.values()))