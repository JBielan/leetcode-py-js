class Solution:
	def isAlienSorted(self, words, order: str) -> bool:
		# nested list comprehension gives indexes of particular chars in Alien Dict
		words_values = [[order.index(char) for char in list(word)] for word in words]
		# [[0, 6, 1, 1, 14], [1, 6, 6, 19, 4, 14, 5, 6]] for the first example

		while len(words_values) > 1:
			'''
			First word is compared with the second and if it's before, we remove it from the list. 
			When 1 word is left, it means all words are in order. 
			'''
			for i in range(len(words_values[0])):
				if words_values[0][i] > words_values[1][i]:
					return False
				elif words_values[0][i] < words_values[1][i]:
					words_values = words_values[1:]
					break

				if i == len(words_values[0]) - 1:
					words_values = words_values[1:]
				elif i == len(words_values[1]) - 1:
					return False

		return True