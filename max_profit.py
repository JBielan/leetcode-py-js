class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		buy_price, profit = float('inf'), 0     # set buy_price and profit to the highest and lowest possible options
		for price in prices:
			if price < buy_price: buy_price = price     # in case you find the lowest price, set it as buy_price
			if price - buy_price > profit: profit = price - buy_price       # in case profit is the highest, set it as new profit
		return profit      # return profit after iterating through the whole list