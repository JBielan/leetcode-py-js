class Solution:
    def findWords(self, words):
        first_row = ('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                     'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')

        second_row = ('A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                      'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l')

        third_row = ('Z', 'X', 'C', 'V', 'B', 'N', 'M',
                     'z', 'x', 'c', 'v', 'b', 'n', 'm')

        result = []

        for word in words:  # for every element of words list
            first_word = [char for char in word if char in first_row]  # word constructed from first_row letters
            second_word = [char for char in word if char in second_row]  # and so on
            third_word = [char for char in word if char in third_row]

            if len(first_word) == len(
                    word):  # if length is the same, it means only letters from first row were necessary
                result.append(word)  # add word to the list
            elif len(second_word) == len(word):  # and so on
                result.append(word)
            elif len(third_word) == len(word):
                result.append(word)

        return result