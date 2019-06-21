class Solution:
    def toGoatLatin(self, S: str) -> str:
        sentence = S.split(' ')  # create a list of words
        for i in range(len(sentence)):  # iterate through all indexes
            if sentence[i][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:  # if word starts with a vovel
                sentence[i] += 'ma'  # add ma in the end
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0] + 'ma'  # if not, put first letter in the end and add ma

            sentence[i] += 'a' * (i + 1)  # in the end add as many 'a' as index + 1

        return ' '.join(sentence)  # join words to the string again