class Solution:
	def decompressRLElist(self, nums: List[int]) -> List[int]:
		'''
		Generally the description is very bad. Just look at the example and you'll get what it is about.
		'''
		res = []
		for i in range(0, len(nums), 2):        # from first to second last by every 2
			res += nums[i]*[nums[i+1]]      # multiply first element by array with second element and add it to the result

		return res      # return result