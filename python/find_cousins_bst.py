class Solution(object):
	def isCousins(self, root, x, y):
		"""
		:type root: TreeNode
		:type x: int
		:type y: int
		:rtype: bool
		"""
		self.ans = []       # by making ans Solution class atributes, you've got access without passing it to the function
		def DFS(node,x,k,parent):
			"""
			http://mishadoff.com/blog/dfs-on-binary-tree-array/ - read why it's so crucial
			"""
			if node.val==x:     # when the node is find - remember x might be x or y
				self.ans.append(k)      # append level to the list
				self.ans.append(parent.val)     # along with the parent value
			# else traverse the tree in a breadth first fashion
			else:
				if node.left:
					DFS(node.left,x,k+1,node)
				if node.right:
					DFS(node.right,x,k+1,node)

		# find the value for x and y
		DFS(root,x,0,root)
		DFS(root,y,0,root)

		# you can check the ans table to make it more clear
		#print(self.ans)

		# return whether x and y has the same k level and different parent
		return self.ans[0]==self.ans[2] and self.ans[1]!=self.ans[3]