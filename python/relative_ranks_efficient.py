class Solution:
	def findRelativeRanks(self, nums: List[int]) -> List[str]:
		"""
		At the first place nums and initial indexes are zipped: zip(nums, range(len(nums))).
		Secondly zipped object is sorted and enumerated to know places.
		In the end we just set score so nums[initial_index] as place + 1 (place starts from 0) in string type.
		For the podium Gold, Silver and Bronze medals are given away according to the place. '
		"""
		for place, (number, initial_index) in enumerate(sorted(zip(nums, range(len(nums))), reverse=True)):
			nums[initial_index] = str(place + 1) if place > 2 else ["Gold Medal", "Silver Medal", "Bronze Medal"][place]
		return nums