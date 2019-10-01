class Solution:
	def hasAlternatingBits(self, n: int) -> bool:
		binary = bin(n)     # string representation of binary number like 0b10 is 2
		for i in range(2, len(binary ) - 1):        # starts from second idx and end at next-to-last
			if binary[i] == binary[i + 1]:      # if adjacent bits are the same
				return False        # return False

		return True     # outside of the loop if False wasn't returned, return True
