class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s))+'#'+s
        return enc

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j =i
            while s[j] != '#':
                j += 1
            print(s[i:j])
            l = int(s[i:j])

            temp = s[j+1:j+l+1]
            res.append(temp)
            i = j+l+1
        return res


