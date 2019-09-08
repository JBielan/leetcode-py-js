class Solution:
	def search(self, nums, target):
		"""
		Binary search is based on a concept of left and right border (l, r).
		At the beginning start and end of an array is taken and a point between them is checked.
		If the middle point is bigger, then just set right border to mid - 1, lowering the area of search.
		If the middle point is smaller, just set left border to mid + 1 with the same effect.
		When borders pass eachother, it means there was no target so loop should be stopped and -1 returned.
		"""
		l, r = 0, len(nums) - 1
		while l <= r:
			mid = l + (r - l) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				l = mid + 1
			else:
				r = mid - 1

		return -1
