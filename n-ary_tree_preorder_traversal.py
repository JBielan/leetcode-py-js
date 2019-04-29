class Solution:
	def preorder(self, root):
		if not root:
			return []       # return empty list in case of empty Node object
		result = [root.val]     # add first node
		for child in root.children:     # iterate through all children
			result.extend(self.preorder(child))     # repeat the process but root is now child
													# this way you can go through the whole tree
		return result
