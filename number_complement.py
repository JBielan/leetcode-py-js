class Solution:
	def findComplement(self, num: int) -> int:
		return int(''.join( [str(abs(int(x)-1)) for x in bin(num)[2:]] ), 2)
	'''
	First of all list comprehension creates a string with inverted 1 and 0. Secondly int(bin, 2) converts binary number into integer.
	'''