


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        x = list(palindrome)
        if len(palindrome) == 1:
            return ""
        for i in range(len(x)):
            if x[i] != 'a':
                x[i] = 'a'
                break
        if x[::-1] == x:
            y = palindrome[0:len(palindrome)-1] + 'b'
            return y
        x = ''.join(x)
        return x



