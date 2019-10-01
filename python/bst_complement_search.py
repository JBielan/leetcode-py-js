class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        stack, seen = [root], set()

        while stack:
            curr = stack.pop()
            # If we've seen k - curr.val,
            # we have k - curr.val + curr.val = k
            if k - curr.val in seen:
                return True
            seen.add(curr.val)

            # Visit children
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return False