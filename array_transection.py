class Solution:
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		nums1, nums2 = list(set(nums1)), list(set(nums2))     # creates distinct lists with numbers
		i = 0
		while i < len(nums1):       # as long as all nums1 will be checked
			if nums1[i] in nums2:       # if item is in second list
				i += 1      # just go to the next item
			else:
				nums1 = nums1[:i] + nums1[i + 1:]       # remove it if it's not

		return nums1        # return the rest