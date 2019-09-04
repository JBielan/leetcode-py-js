class Solution:
	def findJudge(self, N: int, trust: List[List[int]]) -> int:
		'''
		The idea is to find the suspect and check whether everyone trusts to him.
		'''
		believers = set([x[0] for x in trust])      # list all citizens who trust somebody
		suspect = [x for x in range(1, N+1) if x not in believers]      # judge can't trust anybody
		if len(suspect) != 1:       # if everyone trusts sb or more than 1 citizens don't trust anybody
			return -1       # return -1 because it's impossible to find a judge
		trust_check = [False for x in range(1, N+1)]        # map to those who trust to suspect
		trust_check[suspect[0] - 1] = True      # suspect doesn't trust anybody
		for connection in trust:
			if connection[1] == suspect[0]:     # if someone trust to suspect
				trust_check[connection[0] - 1] = True       # set his trust_check to True

		if all(trust_check):        # if everyone trust to suspect
			return suspect[0]       # return its number
		else:
			return -1       # otherwise there's no judge