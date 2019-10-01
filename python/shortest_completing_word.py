class Solution:
	def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
		chars = [ch.lower() for ch in licensePlate if ch.isalpha()]     # list comprehension creates only lower case letters
		chars = ''.join(chars)      # turn the list into string
		words.sort(key=len)     # put words from the shortest

		for word in words:      # for every word
			temp = chars        # create temporary string of chars to remove letters from it
			for char in word:       # for every caracter in word
				temp = temp.replace(char, '', 1)        # remove first occurance of a char
				if len(temp) == 0:      # if all characters are removed
					return word     # the word will be the shortest with all chars from licensePlate