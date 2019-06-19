class Solution:
	def removeDuplicates(self, S: str) -> str:
		i = 0
		while i < len(S) - 1:       # while is necessary to check the length after every loop
			if S[i] == S[i + 1]:
				S = S[:i] + S[i+2:]     # remove duplicates
				if i > 0:
					i -= 2      # in every case except i=0
				else:
					i -= 1      # for i=0 to remain on 0, only -1 is necessary

			i += 1      # go at the next place of the list

		return S