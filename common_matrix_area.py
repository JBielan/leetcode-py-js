class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops==[]:return m*n
        min_col=ops[0][1]
        min_row=ops[0][0]
        for op in ops:
            min_row=min(min_row,op[0])
            min_col=min(min_col,op[1])
        return min_row*min_col