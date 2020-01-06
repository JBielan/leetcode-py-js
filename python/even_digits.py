class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        '''
        For faster execution use list comprehension. It creates a table with as many ones as there are even digits numbers.
        To calculate number of digits it's necessary to convert int into string as intigers don't have len method.
        '''
        return len([1 for number in nums if len(str(number)) % 2 == 0])