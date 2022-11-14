class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        a = a[::-1]
        a = " ".join(a)
        return a