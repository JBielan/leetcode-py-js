class Solution:
	def maximum69Number (self, n: int) -> int:
		'''
		replace(x, y, n) is string method which can replace first n occurences of string x to string y
		'''
		return int(str(n).replace('6','9',1))