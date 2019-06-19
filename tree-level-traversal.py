class Solution:
	def levelOrder(self, root: 'Node'):
		queue = [root] if root else []      # set first node or None in case of empty tree
		result = []     # results will be stored here

		while queue:        # as long as there are any items in queue
			result.append([node.val for node in queue])     # add value of every node in queue
			queue = [child for node in queue for child in node.children]        # for every node in queue add its children - nested list comprehension

		return result
