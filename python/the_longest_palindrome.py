from collections import Counter

class Solution:
	def longestPalindrome(self, s: str) -> int:
		"""
		Generally everytime you try to count occurrences, Counter is very handy and efficient way to do it.
		Counter list(s) counts occurences very fast and store it in Counter object (kind of dictionary).
		Then it's just enough to count number of pairs - (value // 2) and add double to the result.
		In the end just check whether it's possible to insert center. If so, just add 1 to the result.
		"""
		res, center, count = 0, False, Counter(list(s))
		for key, value in count.items():
			if not center and value % 2 == 1:
				center = True
			res += (value // 2) * 2

		return res if not center else res + 1