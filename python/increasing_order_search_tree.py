class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        def inorderTraversal(root):
            res = []  # nodes values will be stored here
            if root:  # if there is any root, otherwise it's None
                res = inorderTraversal(root.left)  # go to the left and run the function again
                res.append(root.val)  # when there's no left, add value to the list
                res = res + inorderTraversal(root.right)  # add right side to the values from left
            return res

        nodes = inorderTraversal(root)  # returns values in-order

        # now the inly thing is to add them as required
        result_tree = TreeNode(nodes[0])  # creates new tree
        node = result_tree  # set node as the beginning of the tree

        for i in range(1, len(
                nodes)):  # it's important to start iterate from the second element, that's way range(1, len(nodes))
            node.right = TreeNode(nodes[i])  # always add new node to the right
            node = node.right  # set node to the one on the right

        return result_tree