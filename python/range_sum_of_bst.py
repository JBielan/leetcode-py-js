# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def sum_tree(root, L, R, total):
            if root.left:  # in case there is a left noode
                sum_tree(root.left, L, R, total)  # call sum_tree on the left node

            if root.val >= L and root.val <= R:  # if value between L and R inclusive
                total.append(root.val)  # add it to the list
            if root.right:
                sum_tree(root.right, L, R, total)  # if there's right node, call function on it

            return total  # when there isn't right and left node, just return a list

        total = []
        return sum(sum_tree(root, L, R, total))  # return the sum of the list

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

As well feel free to follow my account for daily coding solutions and machine-learning/data-science projects:
https://github.com/JBielan

May the code be with you!
"""