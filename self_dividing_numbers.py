class Solution:
	def selfDividingNumbers(self, left: int, right: int):
		result = []     # results will be stored in this list
		for i in range(left, right + 1):        # i will represent all prospects
			count = 0
			string_num = str(i)     # turning int into string to be able to get all digits
			length = len(string_num)
			for digit in string_num:
				if int(digit) != 0 and i % int(digit) == 0:     # digit can't be zero and number has to be divided by digit
					count += 1
				else:
					break       # abandon particular number when conditions aren't met (break for digit loop and get next i)

			if count == length:
				result.append(i)        # when count equals length so all digits where checked, add number to result list

		return result