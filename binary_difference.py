class Solution:
    def binaryGap(self, N: int) -> int:
        idxs = [i for i, x in enumerate(list(bin(N))) if x == "1"]      # list comprehension gets all indexes of 1
        if len(idxs) > 1:      # if there's some difference
            diffs = [abs(j-i) for i,j in zip(idxs, idxs[1:])]       # list comprehension calculates differences
            return max(diffs)       # return max diff
        else:
            return 0        # if there's 1 or 0 zeros, just return 0