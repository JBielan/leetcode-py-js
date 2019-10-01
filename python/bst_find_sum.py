class Solution(object):
	def findTarget(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: bool
		"""
		# queue has to be type of list because order is important
		# seen is set because order doesn't matter and it's faster
		queue, seen = [root], set()

		while queue:        # as long as there's any node in a queue
			curr = queue.pop()      # pop removes and returns last value from the queu
			if k - curr.val in seen:        # k-curr.val in seen means there are two wanted numbers
				return True
			seen.add(curr.val)      # add current number to seen (add because seeen is typo of set)

			# Preorder tree traversal (root, left, right)
			if curr.left:
				queue.append(curr.left)
			if curr.right:
				queue.append(curr.right)

		return False        # if all nodes have been visited without success return False