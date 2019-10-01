class Solution:
	def flipAndInvertImage(self, A):
		return [[abs(x - 1) for x in i] for i in [i[::-1] for i in A]]
