class Solution:
	def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
		'''
		The gist is to save best just after adding 1 to count. Probably that causes only 50% acceptance.
		'''
		count = 0
		best = 0
		for bit in nums:        # for every number in nums
			if bit == 1:        # if bit equals 1
				count += 1      # add 1 to count
				if count > best:        # very important to put this statement here and not in else clause
										# in the second case for arrays ended with 1 best wouldn't be saved
					best = count
			else:
				count = 0


		return best     # return best when loop goes through all nums