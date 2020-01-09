class Solution:
	def subtractProductAndSum(self, n: int) -> int:
		n_str = str(n)      # to iterate through digits, the number should be string
		p, s = 1, 0     # product starting point is 1 and sum 0

		for digit in n_str:     # for every digit in a number
			p *= int(digit)     # multiply product by a digit
			s += int(digit)     # and add a digit to the sum

		return p - s        # return the difference