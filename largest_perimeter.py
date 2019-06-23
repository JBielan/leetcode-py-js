class Solution:
	def largestPerimeter(self, A) -> int:
		A.sort()        # sort from the smallest to the biggest
		for i in range(len(A) - 1, 1, -1):      # from last element till index 2 to always get 3 sides
			if A[i-2] + A[i-1] > A[i]:      # if 2 smaller sides are bigger than the biggest
				return A[i-2] + A[i-1] + A[i]       # return the sum
		return 0