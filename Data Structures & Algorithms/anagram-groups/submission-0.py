class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmaps = {}
        for i in strs:
            anagram = ''.join(sorted(i))
            if anagram not in hashmaps:
                hashmaps[anagram] = []
            hashmaps[anagram].append(i)
        return list(hashmaps.values())
