class Solution:
	def replaceElements(self, arr: List[int]) -> List[int]:
		res, greatest = [], 0

		for num in arr[::-1]:       # for every number starting from the end
			if greatest < num:      # if number is bigger than current greatest
				greatest = num      # set this number as greatest
			res.append(greatest)        # add greatest to the result list

		''' 
		This is the most important moment. 
		Right now the result is inverted and it has one element more (last gratest is doubled)
		Small transformation is needed:
		[:-1] cuts last greatest
		[::-1] inverts the result
		+ [-1] adds -1 in the end
		'''
		return res[:-1][::-1] + [-1]