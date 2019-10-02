class Solution:
    def reverse(self, x: int) -> int:
        '''
		The easiest way to do it is turning number into string and than operate on it.
		'''
        if x >= 0:  # in case there's no need to treat minus
            x = int(str(x)[::-1])  # just turn number into string, reverse it and turn it back into int
        else:
            x = int('-' + str(abs(x))[::-1])  # otherwise get absolute value, do the same and add minus at the beginning

        if (-2) ** 31 <= x <= 2 ** 31 - 1:
            return x
        else:  # in case x is smaller or bigger than required range, return 0
            return 0
