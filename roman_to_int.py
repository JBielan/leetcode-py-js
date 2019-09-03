class Solution(object):
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:       # in case of 0
			return 0
		dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}        # map for values
		n = len(s)
		total = dic[s[n-1]]     # set total as last sign
		for i in range(n-1,0,-1):       # loop from last to first index
			# take two int numbers from adjacent roman signs
			current = dic[s[i]]
			prev = dic[s[i-1]]
			# and check which one is bigger
			# if previous is bigger or equal, add it to sum
			# otherwise less it according to roman numerals rules
			# i.e IX = 10-1
			total += prev if prev >= current else -prev

		# after calculating all values, return the result
		return total