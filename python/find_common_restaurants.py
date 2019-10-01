class Solution:
	def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
		common = set(list1).intersection(set(list2))        # sets are great to find common items
		if len(common) == 1:        # in case there's only 1 common, just return it
			return [common.pop()]
		all_common = []     # we need common restaurants with sum of indexes
		for restaurant in common:       # calculate sum of idxs for every common restaurant
			all_common.append([list1.index(restaurant) + list2.index(restaurant), restaurant])

		m = min(all_common)[0]      # find minimum value for sum
		idxs = [i for i, j in enumerate(all_common) if j[0] == m]       # find indx with minimum sum
		res = []        # prepare a list for results
		for idx in idxs:        # prepare result with names of the restaurants
			res.append(all_common[idx][1])
		return res      # return result