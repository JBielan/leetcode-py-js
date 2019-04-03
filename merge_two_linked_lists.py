class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """ Starting a new list with Node0 set to start and current - current will be changed so we need start for return statement"""
        start = current = ListNode(0)

        # While l1 and l2 are not None (lists didn't end yet)
        while l1 and l2:
            # We always link to equal or bigger number because lists are sorted
            if l1.val < l2.val:
                current.next = l1  # Link is created here
                l1 = l1.next  # We go to the next item for l1 list
            else:
                current.next = l2  # Link is created here
                l2 = l2.next  # l2 stores next item

            current = current.next  # Iteration of the main variabl

        current.next = l1 or l2  # There might be one item too less in the end and it solves it
        return start.next