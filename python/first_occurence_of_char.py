from collections import Counter

class Solution:
	def firstUniqChar(self, s: str) -> int:
		"""
		Counter is the fastest way to count occurrences. It creates Counter object simillar to dictionary.
		key is an item from a string and value is the number of occurrences.
		It's enough to return index of key with value 1.
		If there isn't such key, it means there's no unique character so return -1.
		"""
		for key, value in Counter(s).items():
			if value == 1: return(s.index(key))
		return -1