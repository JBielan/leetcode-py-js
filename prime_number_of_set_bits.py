class Solution:
	def countPrimeSetBits(self, L: int, R: int) -> int:
		def is_prime(n):
			if n > 1:       # negative and 0 or 1 aren't prime
				for i in range(2, n):       # to check if there are any divisors
					if n % i == 0:      # if there's divisor
						return False        # i is not prime

				else: return True       # if the whole loop ends without executing if, i is prime

			else:
				return False        # if it's < 1 it's not prime

		count = 0
		for j in range(L, R + 1):       # R is inclusive so it has to be + 1
			n_ones = len([1 for bit in list(bin(j))[2:] if bit == '1'])     # list comprehension creates a list of ones and checks its length
			if is_prime(n_ones):
				count += 1      # add 1 if the number is prime

		return count