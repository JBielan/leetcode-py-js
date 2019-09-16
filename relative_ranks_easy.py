class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        """
        This solution is very easy to understand but it's not optimal in terms of execution time.
        """
        order = sorted(nums, reverse=True)  # store results in descending order
        place = 1  # start counting places
        for score in order:  # iterate from first to last place
            if place > 3:  # after podium
                nums[nums.index(score)] = str(place)  # find index of score and replace it with its place as string
            elif place == 1:
                nums[nums.index(
                    score)] = "Gold Medal"  # for the first place give gold medal and analogically for the whole podium
            elif place == 2:
                nums[nums.index(score)] = "Silver Medal"
            elif place == 3:
                nums[nums.index(score)] = "Bronze Medal"
            place += 1  # in the end before checking next result go to the next place

        return nums  # return nums list with places instead of results