class Solution:
	def fairCandySwap(self, A, B):
		half_difference = (sum(A) - sum(B)) // 2     # half of the difference because diff is counted twice (one increase, second decrease)
		for number in A:        # for every number in A
			if number - half_difference in B:       # check whether difference is in B
				return [number, number - half_difference]       # if it is, return number which should be exchanged