class Solution:
	def distributeCandies(self, candies: int, num_people: int):
		dist = [0 for i in range(num_people)]       # list with as many zeros as there are people
		give_away = 1       # giving away starts with 1
		i = 0       # indexing strats from the first element

		while candies > 0:      # as long as there are any candies
			if give_away <= candies:        # if there's more candies than give_away
				dist[i] += give_away        # distribute candies to the person
			else:
				give_away = candies     # if there's less candies, just give the rest
				dist[i] += give_away

			candies -= give_away        # decrease number of candies after every give_away
			give_away += 1      # prepare next give_away
			if i != len(dist) - 1:      # go to the next index if i isn't equal last index
				i += 1
			else:
				i = 0       # if it's last index, just go to the beginning

		return dist