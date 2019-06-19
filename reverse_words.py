class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')  # creates a list of words
        reverse = []  # reversed words will be stored here
        for word in s:
            reverse.append(word[::-1])  # adds reversed word to the reverse list

        result = ' '.join(reverse)  # joins words with a space

        return result
