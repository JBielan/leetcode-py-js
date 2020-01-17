import string

class Solution:
	def freqAlphabets(self, s: str) -> str:
		mapping = {}        # dictionary with mapping like {'1':'a'}
		chars = string.ascii_lowercase      # all lowercase english letters

		for i in range(len(chars[:9])):     # for every letter from a to i
			mapping[str(i+1)] = chars[i]                # create a mapping

		for i in range(len(chars[9:])):     # for every letter from j to z
			mapping[str(i+10)+'#'] = chars[i+9]     # as well create a mapping

		res = ""        # result will be stored here
		i = 0
		while i < len(s):       # while loop because index will be manipulated
			if i < len(s) - 2:      # if it's not the end of the string
				if s[i+2] != '#':       # for non-has letters
					res += mapping[s[i]]        # add this letter
					i += 1      # and move forward by 1
				else:       # for hash letters
					res += mapping[s[i:i+3]]        # add this latter
					i += 3      # and move forward by 3 because those letters have length 3
			else:       # if it's the end of the string
				res += mapping[s[i]]        # treat it as non-hash letters and add it to the result
				i += 1      # move one index forward

		return res      # return the result