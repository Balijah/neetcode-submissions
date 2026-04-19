class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for words in strs:
            countofletters = [0] * 26

            for character in words:
                countofletters[ord(character) - ord("a")] += 1
            
            res[tuple(countofletters)].append(words)
        
        return (list(res.values()))