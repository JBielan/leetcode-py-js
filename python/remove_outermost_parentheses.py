class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        parts = []
        left_n = 0
        right_n = 0

        # [j+1:i] will be slice getting parts without beginning and end
        j = 0

        for i in range(len(S)):
            if S[i] == "(":
                left_n += 1  # add 1 when left parenthesis
            else:
                right_n += 1  # add 1 when right

            if left_n == right_n:
                parts.append(S[j + 1:i])  # add part when left_n = right_n
                j = i + 1  # because next first item will be cut, i + 1 gives j += 2 total

        return "".join(parts)  # join string items without space and return

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

As well feel free to follow my account for daily coding solutions and machine-learning/data-science projects:
https://github.com/JBielan

May the code be with you!
"""