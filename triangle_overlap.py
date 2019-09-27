class Solution:
	def isRectangleOverlap(self, rec1, rec2):
		'''
		To form an overlapped rectangle both overlapping width and height must be positive.
		'''
		return True if min(rec1[2], rec2[2]) - max(rec1[0], rec2[0]) > 0 and min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]) > 0 else False