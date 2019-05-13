# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        current = head  # current node will be used for iteration
        count = 0
        while current:  # as long as there's next node
            count += 1  # count number of nodes
            current = current.next  # and go to the next node

        middle_idx = int(count / 2)  # calculate middle index - int used for rounding it down

        current = head  # let's start from the beginning of the list
        for _ in range(middle_idx):  # with loop with middle_idx steps
            current = current.next  # go further at every step as long as you reach middle node

        return current  # return this node
