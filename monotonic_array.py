class Solution:
	def isMonotonic(self, A: List[int]) -> bool:
		if len(A) == 1: return True     # in case of 1 element list

		# check whether list is decreasing or increasing
		increasing, decreasing = False, False

		i = 0
		while not increasing and not decreasing:        # as long as both are False
			if A[i] < A[i + 1]:
				increasing = True       # if first 2 elements are increasing set as increasing
			elif A[i] > A[i + 1]:
				decreasing = True       # similarly for decreasing
			else:       # if they are equal, just go to the next element
				if i < len(A) - 2:      # if it's possible, go to the next element
					i += 1
				else:       # if it's last element (e.g. [1, 1, 1]) return True
					return True

		length = len(A)     # array length doesn't change so let's set it to variable

		for j in range(i, length - 1):      # go from i'th element to second last
			if increasing:
				if A[j] > A[j + 1]:     # if it's increasing and next element is smaller, return False
					return False
				elif j == length - 2:       # if it's second last index just return True as it's the end of array
					return True
			elif decreasing:        # similarly for decreasing
				if A[j] < A[j + 1]:
					return False
				elif j == length - 2:
					return True