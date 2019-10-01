# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def find_leaves(root):  # inorder traversal with condition before adding to res
            res = []
            if root:  # as long as it's not the end of the tree
                res = find_leaves(root.left)  # go always left
                if not root.left and not root.right:  # condition for leaves
                    res.append(root.val)  # add to res if it's leave
                res = res + find_leaves(root.right)  # add to results leaves from right branches
            return res  # return results list when it's end

        if find_leaves(root1) == find_leaves(root2):  # compare 2 lists
            return True
        else:
            return False
