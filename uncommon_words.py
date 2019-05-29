class Solution:
	def uncommonFromSentences(self, A: str, B: str):
		both = A.split(' ') + B.split(' ')      # create a list of words
		return [x for x in both if both.count(x)==1]         # standard list comprehension