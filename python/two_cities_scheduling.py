class Solution:
	def twoCitySchedCost(self, costs: List[List[int]]) -> int:
		differences = [[costs[i][0] - costs[i][1], i] for i in range(len(costs))]       # list comprehension returning
																						# differences with indexes
		differences = sorted(differences, key=lambda x: x[0])       # sort differences by first element so difference

		result = 0
		'''
		First half of sorted differences should go to A and second half should go to B.
		Loop below iterate through indexes of both halves.
		'''
		for i, j in zip( range(int(len(differences) / 2)), range(int(len(differences) / 2), len(differences)) ):
			result += costs[differences[i][1]][0] + costs[differences[j][1]][1]
		return result