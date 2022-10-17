class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = dict()
        for i in range(97, 123):
            a[i]=0
        for i in sentence:
            i=ord(i)
            a[i]+=1
        for i in a.values():
            if i == 0:
                return False
        return True