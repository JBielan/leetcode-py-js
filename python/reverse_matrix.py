class Solution:
    def transpose(self, A):
        rows = len(A)  # number of rows
        columns = len(A[0])  # number of columns
        temporary = []
        result = []
        for i in range(columns):
            for j in range(rows):
                temporary.append(
                    A[j][i])  # the algorithm goes as follow: A[0][0], A[1][0], A[2][0], A[0][1], A[1][1] etc
            result.append(temporary)  # add every row
            temporary = []  # clear temp list so it can be used again

        return result