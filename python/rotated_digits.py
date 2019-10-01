class Solution:
	def rotatedDigits(self, N: int) -> int:
		count = 0
		for n in range(1, N + 1):       # for 10 it's [1:10]
			n = str(n)      # let's make the checking number a string to be able to use "in" operator
			if '3' not in n and '4' not in n and '7' not in n and not \     # if there isn't 3,4,7 digit and not all digits are 0,1,8 - the number is "good"
			all(c in '018' for c in n):
				count += 1      # so add 1 to the counter

        return count