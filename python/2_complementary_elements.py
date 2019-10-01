class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		memory = {}     # dictionary where missing numbers will be stored with pairing indexes
		for i in range(len(numbers)):       # iterate through the whole list
			if numbers[i] not in memory:        # it looks for dic keys, so missing numbers
				memory[target - numbers[i]] = i     # if the number isn't mising, add its target together with its index
			else:
				return [memory[numbers[i]] + 1, i + 1]      # if we found the number, just return index of complementary number and current number
															# plus 1 because it's not about index but order