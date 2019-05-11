class Solution:
	def reverseWords(self, s: str) -> str:
		return ' '.join([word[::-1] for word in s.split(' ')])      # s.split(' ') creates a list of words,
        # list comprehension diverts symbols within a word and ' '.join() joins them back into a string
