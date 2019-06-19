class Solution:
	def sumEvenAfterQueries(self, A, queries):
		even_sums = []      # sums will be stored here
		for query in queries:       # loop over queries
			A[query[1]] += query[0]     # required change
			even = [x for x in A if x % 2 == 0]     # creates a list of even numbers - list comprehension
			even_sums.append(sum(even))     # add sum to the list of sums

		return even_sums