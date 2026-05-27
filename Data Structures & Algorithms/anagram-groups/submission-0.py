class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs: 
            alph = [0]  * 26
            for letter in word: 
                alph[ord(letter) - ord('a')] += 1

            key = tuple(alph)

            if key not in anagrams: 
                anagrams[key] = []
            
            anagrams[key].append(word)
        
        print(anagrams)
        return list(anagrams.values())
