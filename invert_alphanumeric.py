class Solution:
	def reverseOnlyLetters(self, S: str) -> str:
		not_alpha = [[i, S[i]] for i in range(len(S)) if not S[i].isalpha()]        # create a list of indexes and not_alpha elements
		inverted = [char for char in S if char.isalpha()][::-1]     # invert alpha elements
		for not_char in not_alpha:      # for every not alpha
			inverted.insert(not_char[0], not_char[1])       # insert it to the old place

		return ''.join(inverted)        # return the list as string