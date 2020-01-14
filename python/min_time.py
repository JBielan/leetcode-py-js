class Solution:
	def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
		return sum(( max(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1])) for i in range(len(points) - 1) ))
		'''
		List comprehension creates tuple with minimum lengths from points and sum it in the end.
		'''