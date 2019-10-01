class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		# let's distinguish first 2 levels to start with the algorithm from the third step
		if numRows == 0:
			return []
		elif numRows == 1:
			return [[1]]

		"""
		The idea is to iterate through last row, add sums to the next_row variable
		and in the end just add side 1s to fit the triangle.
		"""
		res = [[1], [1,1]]      # assuming numRows is 2 or more
		i = 1       # just to count number of rows
		while i < numRows - 1:
			next_row = []       # preparing variable to store new row
			for j in range(len(res[-1]) - 1):       # iteration through last row except last element as j+1 index will be called
				next_row.append(res[-1][j] + res[-1][j+1])      # creation of next_row without 1s on sides
			next_row = [1] + next_row + [1]     # adding 1s on sides
			res.append(next_row)        # adding a whole new row to the result
			i += 1      # another row was added so i should be incremented by 1

		return res