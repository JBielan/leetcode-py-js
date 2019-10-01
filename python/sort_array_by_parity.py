class Solution(object):
    def sortArrayByParity(self, A):
        even = []
        odd = []
        for number in A:
            if number % 2 == 0:         # if remainder is equal 0, the number is even
                even.append(number)     # add to even
            else:
                odd.append(number)      # when remainder isn't equal 0, it's odd so add to odd

        return even + odd               # + sign joins to lists

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

As well feel free to follow my account for daily coding solutions and machine-learning/data-science projects:
https://github.com/JBielan

May the code be with you!
"""