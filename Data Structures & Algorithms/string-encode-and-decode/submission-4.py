class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        ret = []
        while i<len(s):
            j=i
            while s[j] != '#':
                j+=1
            l = int(s[i:j])
            i = j+1
            j = i+l
            word = s[i:j]
            ret.append(word)
            i=j
        return ret