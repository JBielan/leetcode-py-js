class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1

        results = [0, 1]

        for i in range(1, N):
            results.append(sum(results[-2:]))

        return results[-1]
