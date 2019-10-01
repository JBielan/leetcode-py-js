class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"

        if n == 2:
            return "11"

        current = "11"      # If function wasn't returned yet, current is "11" and it's at least step 3
        for _ in range(1, n - 1):           # "_" is variable we won't use. The only thing is to get n-2 steps
            count = 1                       # There will be at least one occurrence
            new_string = ""                 # Another variable needed to not operate directly on current
            for j in range(len(current)):   # Iteration over current string to get the next one
                if j != len(current) - 1:   # If not last index
                    if current[j] == current[j + 1]:
                        count += 1          # Add one to count as long as there's another character
                    else:
                        new_string += str(count) + current[j]   # add "count and say" part for current j
                        count = 1                               # Reset count when new char was found
                else:                                           # Last character scenario
                    new_string += str(count) + current[j]       # add last "count and say" for current step
            current = new_string
        return current

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

As well feel free to follow my account for daily coding solutions and machine-learning/data-science projects:
https://github.com/JBielan

May the code be with you!
"""