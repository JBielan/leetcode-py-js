class Solution:
	def findTheDifference(self, s: str, t: str) -> str:
		"""
		As long as first t element is in s, remove first occurence in s and t.
		When it's not remove this element.
		"""
		while True:
			if t[0] not in s:
				return t[0]
			s = s.replace(t[0], "", 1)
			t = t[1:]