class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:int(len(s)/2)].lower()
        b = s[int(len(s)/2):].lower()
        ca = 0
        cb = 0
        for i in range(int(len(s)/2)):
            if a[i] == 'a' or a[i] == 'e' or a[i] == 'o' or a[i] == 'i' or a[i] == 'u':
                ca+=1
            if b[i] == 'a' or b[i] == 'e' or b[i] == 'o' or b[i] == 'i' or b[i] == 'u':
                cb += 1
        
        if cb == ca:
            return True
        else:
            return False