class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        number = x
        while (number > 0):
            reminder = number % 10  # getting last digit (units) from the number
            reverse = (reverse * 10) + reminder  # creating new reversed number
            number = number // 10  # getting the number without last digit (cutting units)

        # x has to be bigger than 0 because negative numbers don't meet the criteria
        if x >= 0 and x == reverse:
            return True
        else:
            return False

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

Remember to have fun in coding journey. Thank you!
"""