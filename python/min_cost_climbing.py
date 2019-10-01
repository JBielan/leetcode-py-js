class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        if l <= 1 or l > 1000:
            return -1

        tc = l * ['']  # total minimum cost at each index
        tc[0], tc[1] = cost[0], cost[1]  # initialize the first two items

        for i in range(2, l):
            tc[i] = min(tc[i - 2], tc[i - 1]) + cost[i]

        return min(tc[-2], tc[-1])