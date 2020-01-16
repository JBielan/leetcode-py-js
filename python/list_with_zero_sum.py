class Solution:
	def sumZero(self, n: int) -> List[int]:
		'''
		Create a list [1 to n/2] and return [1 to n/2] + [1 to n/2]*(-1) when n is even or with additional [0] when n is odd.
		'''
		return [i for i in range(1, int(n/2 + 1))] + [i*(-1) for i in [i for i in range(1, int(n/2 + 1))]] if n % 2 == 0 else [i for i in range(1, int(n/2 + 1))] + [i*(-1) for i in [i for i in range(1, int(n/2 + 1))]] + [0]