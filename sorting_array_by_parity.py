class Solution:
	def sortArrayByParityII(self, A):
		odd = [x for x in A if x % 2 != 0]      # separate odd numbers
		even = [x for x in A if x % 2 == 0]     # separate even numbers

		result = []

		for x, y in zip(even, odd):
			result.append(x)
			result.append(y)        # join even and odd numbers starting from even

		return result