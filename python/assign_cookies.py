class Solution:
	def findContentChildren(self, g: List[int], s: List[int]) -> int:
		# in case there isn't any cookies or kids
		if not g or not s:
			return 0

		g.sort()
		s.sort()        # both lists are sorted for simplicity
		res = 0

		while len(s) > 0 and len(g) > 0:        # as long as there's cookie or kid
			if s[0] >= g[0]:        # check whether the smallest cookie can be given to the least greedy kid
				res += 1        # if so increment res by 1, remove kid and cookie from the list
				s = s[1:]
				g = g[1:]
			else:
				s = s[1:]       # otherwise it means cookie won't be useful

		return res      # when there isn't cookies or kids just return the result