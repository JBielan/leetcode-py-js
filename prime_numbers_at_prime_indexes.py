from itertools import permutations


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(number):
            '''
            The easiest way to calculate prime number (not the most efficient)
            '''
            return 2 in [number, 2 ** number % number]

        res = 0
        perms = permutations(range(1, n + 1))  # store all permutations in perms variable
        for perm in perms:  # for every permutation
            for i in range(len(perm)):  # for every item in that permutation
                if isPrime(perm[i]) and not isPrime(i + 1):  # break if prime number is not on prime index
                    break
                if i == len(perm) - 1:  # if last item is reached
                    res += 1  # just add 1 to result

        # This solution times out for higher numbers
        return res % (10 ** 9 + 7)  # return result modulo 10^9 + 7 as requested