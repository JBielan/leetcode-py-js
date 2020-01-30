class Solution:
	def convert(self, s: str, numRows: int) -> str:
		'''
		The solution is based on a patern that row increases as long as it reaches numRows - 1 index.
		It then decreases as long as it reaches 0 index. And the pattern repeats.
		'''
		res = [''] * len(s)     # there has to be ready rows * len(s) as max for numRows=1
		row, step = 0, 0        # it starts from zero
		for c in s:     # for every character in the string
			if row == 0:
				step = 1        # go forward when reaching row 0
			elif row == numRows - 1:
				step = -1       # turn back when reaching last index

			res[row] += c       # add character to the row
			row += step     # move forward/backward

		# at this point res is a list of strings for every row
		return ''.join(res)     # join the list of strings in the end