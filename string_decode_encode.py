class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return "b"
        for s in strs:
            for c in s:
                res += str(ord(c))
                res += "a"
            res += "b"

        return res[:-1]

    def decode(self, s: str) -> List[str]:

        if s == "b":
            return []
        if s == "":
            return [""]

        l = s.split("b")
        res = []
        for m in l:
            word = m[:-1].split("a")
            chr_word = [chr(int(w)) for w in word if w]
            word_str = "".join(chr_word)
            res.append(word_str)

        return res
