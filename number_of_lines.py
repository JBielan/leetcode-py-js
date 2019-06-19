import string

class Solution:
	def numberOfLines(self, widths, S) :
		alphabet = string.ascii_lowercase       # list of english characters
		line = 0        # width of single line will be stored here
		lines = 0       # how many full lines have been used
		for letter in S:        # for every letter in a string
			i = alphabet.index(letter)      # find its index in the alphabet
			width = widths[i]       # check its width
			if line + width <= 100:     # if there's enough room
				line += width       # add it to the line
			else:
				lines += 1      # otherwise go to the new line
				line = width        # and add to the new line width of first character

		return [lines + 1, line]        # +1 because it's reaquired to calculate not only full lines
