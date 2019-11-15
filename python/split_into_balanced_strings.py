class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rc, lc, res = 0, 0, 0  # r_count, l_count, result is equal to 0
        for let in s:  # for every letter in string
            if let == 'R':  # if the letter is R, increment r_count
                rc += 1
            else:  # otherwise increment l_count
                lc += 1

            if rc == lc:  # after every letter check whether there's equal amount of R and L
                res += 1  # if so, add 1 to result
                rc, lc = 0, 0  # and reset r_count and l_count

        return res  # return result after iterating through all letters

    ''' This way you store only necessary information and iterate through string once.'''
