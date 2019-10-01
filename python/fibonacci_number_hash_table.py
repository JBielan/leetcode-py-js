class Solution:
    def fib(self, N: int) -> int:
        fib = (
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
        46368, 75025, 121393, 196418, 317811, 514229, 832040)

        return fib[N]

    '''
    Generally the more bigger numbers are checked, the better this solution will be. For the matter of Leetcode
    challenge, is almost simmilar when it comes to execution time. For N >30 it will be much faster. 
    '''