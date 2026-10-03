class Solution:

    def encode(self, strs: List[str]) -> str:
        prefixes = ""
        #for i in range(len(strs)):
         #   prefixes[i] = len(strs[i]) + "#" + strs[i]
        if len(strs) == 0:
            return ""

        for s in strs:
            prefixes += str(len(s)) + "#" + s
        return prefixes

    def decode(self, s: str) -> List[str]:
        pos = 0
        res = []

        while pos < len(s):
            j = pos
            while s[j] != '#':
                j += 1
            length = int(s[pos:j])
            start = j+1
            end = start + length

            res.append(s[start:end])

            pos = end
        return res
            