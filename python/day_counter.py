class Solution:
	def dayOfYear(self, date: str) -> int:
		# map between how many days passed from the beginning of the year
		months_dic = {
			0: 0,
			1: 31,
			2: 59,
			3: 90,
			4: 120,
			5: 151,
			6: 181,
			7: 212,
			8: 243,
			9: 273,
			10: 304,
			11: 334,
			12: 365,
		}

		year, month, day = int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2])        # distill y,m,d in integers

		# leap year occures every 4 years except years divisible by 100 with exception of those divisible by 400
		# when we talk about jan or feb, leap year doesn't change anything so month > 2 rule is added
		if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and  month > 2:
			return months_dic[month - 1] + day + 1      # +1 for leap years because Feb has 29 days instead of 28

		# for the normal years
		else:
			return months_dic[month - 1] + day