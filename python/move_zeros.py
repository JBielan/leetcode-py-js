class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		i = 0       # index for searching
		i_non_zero = 0      # index for non-zero numbers
		while i < len(nums):        # iterate till the end of the list
			if nums[i] != 0:        # if number isn't zero
				nums.insert(i_non_zero, nums.pop(i))        # remove it and put at non-zero index place
				i_non_zero += 1     # prepare non-zero index for next number
			i += 1      # go to the next place