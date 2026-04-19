class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        defdict = defaultdict(list)

        for word in strs:
            sorted_letters = sorted(word)
            sorted_words = "".join(sorted_letters)
            defdict[sorted_words].append(word)
        print(defdict)
        return(list(defdict.values()))