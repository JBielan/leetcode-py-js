class Solution:
	def titleToNumber(self, s: str) -> int:
		"""
		Store values for particular chars in a dictionary.
		Calculate the result from easy formula: char_value * 26**(len - index - 1) for every char
		"""
		dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
			   'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
			   'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
			   'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

		result = 0
		length = len(s)
		for i in range(length-1, -1, -1):
			result += dic[s[i]]*26**(length - i - 1)
		return result