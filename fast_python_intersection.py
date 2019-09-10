from collections import Counter

class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		"""
		First of all Counter counts particular elements for nums1 and nums2 and returns Counter object (something simillar do dict).
		& gets intersection leaving the type as collections.Counter.
		Counter.elements() method creates itertools.chain object (faster unordered list).
		And from here it's enough to use * to unpack values from the chain and put it into [].
		"""
		return [*(Counter(nums1) & Counter(nums2)).elements()]