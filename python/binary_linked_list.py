class Solution:
	def getDecimalValue(self, head: ListNode) -> int:
		binary = ''     # binary representation will be stored here
		while True:     # it's infinite loop but there's break in the end to check the condition in the end
			binary += str(head.val)     # add digit to binary representation
			head = head.next        # make head the next digit
			if head == None:        # if there isn't next digit, break the loop
				break

		return int(binary, 2)       # return int representation of binary number