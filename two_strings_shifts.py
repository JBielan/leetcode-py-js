class Solution:
	def rotateString(self, A: str, B: str) -> bool:
		'''
		Take into account empty strings.
		'''
		if not A and not B:
			return True
		elif A and not B:
			return False
		elif not A and B:
			return False

		A_shifted = A[1:] + A[0]        # first shift
		while A_shifted != A:       # as long as shifted A becomes an old A
			if A_shifted == B:      # if after shifts we get B
				return True
			A_shifted = A_shifted[1:] + A_shifted[0]        # otherwise try another shift

		return False        # return False when B wasn't found in a while loop