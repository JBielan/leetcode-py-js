class Solution:
	def isPalindrome(self, x: int) -> bool:
		'''
		Straight forward but powerful and complete solution. [::-1] is a classic way to invert strings in Python,
		which tells the computer to slice from the beginning till the end [:] but with inverted order [::-1].
		'''
		return str(x) == str(x)[::-1]