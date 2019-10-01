class Solution:
    def findDisappearedNumbers(self, nums):
        '''
        Sets are very fast Python data structures. Whenever order isnt important you can use them to speed-up run-time.
        Firstly it creates a set of numbers from 1 to n and then difference method returns a list of missing numbers.
        '''
        return set(range(1, len(nums) + 1)).difference(set(nums))