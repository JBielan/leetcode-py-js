class Solution:
	def addDigits(self, num: int) -> int:
		while num / 10 >= 1:        # as long as there's 2 digits number
			num = str(num)      # turn num into string to be able to iterate through digits
			temp = 0        # prepare temprary variable to store new num
			for digit in num:       # for every digit
				temp += int(digit)      # add all digits
			num = temp      # set new num

		return num      # return num when while loop break