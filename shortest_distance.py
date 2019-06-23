class Solution:
    def shortestDistance(self, words, word1: str, word2: str) -> int:
        best = len(words)  # length is just big enough number to find smaller
        idx_1 = idx_2 = -1  # -1 because all indexes are bigger
        for i in range(len(words)):  # iterate through the list of words
            if words[i] == word1:
                idx_1 = i  # set index of word1
            elif words[i] == word2:
                idx_2 = i  # set index of word2

            if idx_1 >= 0 and idx_2 >= 0 and best > abs(
                    idx_1 - idx_2):  # if both indexes were find and difference is smaller than best
                best = abs(idx_2 - idx_1)  # set the difference as best

        return best  # return best after the loop