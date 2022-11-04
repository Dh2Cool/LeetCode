class Solution:
    def reverseVowels(self, s: str) -> str:
        j = len(s) -1
        i=0
        temp = ''
        a = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while(i<j):
            if a[i] in vowels and a[j] in vowels:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                i+=1
                j-=1
            elif a[i] not in vowels and a[j] in vowels:
                i+=1
            elif a[i] in vowels and a[j] not in vowels:
                j-=1
            else:
                i+=1
                j-=1
        
        return "".join(a)