class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		"""
		The easiest solution is to buy/sell stock everytime you can get profit.
		For [1,2,3,4,5] scenario the result is the same as buying at day 1 and selling at day 5.
		The result is a sum for list created by list comprehension when transaction occured everytime
		it was profitable (prices[i] > prices[i-1]).
		"""
		return sum(prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] > prices[i - 1])