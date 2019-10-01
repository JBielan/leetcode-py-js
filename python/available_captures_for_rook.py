class Solution:
    def numRookCaptures(self, board) -> int:
        def where_is_rook():  # first of all let's find rook coordinates
            for rank in range(8):  # for every rank
                for column in range(8):  # go all columns
                    if board[rank][column] == 'R':
                        return rank, column  # and return rank and column if there's a rook

        def left(r_rank, r_column):  # check pawns to the left
            for i in range(r_column - 1, -1, -1):  # which columns: 1 before rook column till 0 - reversed
                if board[r_rank][i] == "B":
                    break  # in case of bishop, break and return 0
                elif board[r_rank][i] == "p":
                    return 1  # in case of a pawn return 1

            return 0

        '''
        Repeat the same methodology for right, down and up
        '''

        def right(r_rank, r_column):
            for i in range(r_column + 1, 8):
                if board[r_rank][i] == "B":
                    break
                elif board[r_rank][i] == "p":
                    return 1

            return 0

        def down(r_rank, r_column):
            for i in range(r_rank + 1, 8):
                if board[i][r_column] == "B":
                    break
                elif board[i][r_column] == "p":
                    return 1

            return 0

        def up(r_rank, r_column):
            for i in range(r_rank - 1, -1, -1):
                if board[i][r_column] == "B":
                    break
                elif board[i][r_column] == "p":
                    return 1

            return 0

        counter = 0

        r_rank, r_column = where_is_rook()  # get rook coordinates

        # and count how many pawns it can get
        counter += left(r_rank, r_column)
        counter += right(r_rank, r_column)
        counter += down(r_rank, r_column)
        counter += up(r_rank, r_column)

        return counter

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

As well feel free to follow my account for daily coding solutions and machine-learning/data-science projects:
https://github.com/JBielan

May the code be with you!
"""