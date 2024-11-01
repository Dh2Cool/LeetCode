class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if i+2<len(s):
                if s[i] == s[i+1] and s[i] == s[i+2]:
                    continue
            ans = ans + s[i]
        # print(ans)
        return ans