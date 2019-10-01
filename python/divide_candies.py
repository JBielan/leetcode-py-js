class Solution:
	def distributeCandies(self, candies) -> int:
		n_candies = len(candies)        # number of candies
		n_kinds = len(set(candies))     # number of kinds

		if n_kinds > n_candies / 2:     # if there's more kinds than half of all candies
			return int(n_candies / 2)       # sister will get always half of candies of different kind
		else:       # if there's less kinds
			return n_kinds      # she will get all candies with different kinds
