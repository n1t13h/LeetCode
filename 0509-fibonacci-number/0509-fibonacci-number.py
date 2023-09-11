class Solution:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        if n == 0:
            self.memo[n] = 0
        elif n == 1:
            self.memo[n] = 1
        else:
            self.memo[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.memo[n]