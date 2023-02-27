class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n == 2 or n == 1:
            return 1
        else:
            a = 0
            b = 1
            c = 0
            for i in range(0, n-1):
                c = a+b
                a = b
                b = c
            return c