class Solution:
	def smallestRangeI(self, A, K):
		smallest = min(A)       # smallest value
		biggest = max(A)        # biggest value
		difference = abs(biggest - smallest)        # absolute value of difference

		if difference <= 2*K:   return 0        # you can add up to K and substract up to K, so all digits will be equal

		else:   return difference - 2*K     # when difference is bigger, you can dicrease it by adding K to smallest and substructing K from biggest
