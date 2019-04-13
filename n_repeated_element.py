from collections import Counter

class Solution:
    def repeatedNTimes(self, A) -> int:
        rep_dic = dict(Counter(A))          # Creates dictionary with number of repetitions
        for key in rep_dic:
            if rep_dic[key] == len(A)/2:    # When value equals N, return key
                return key

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

As well feel free to follow my account for daily coding solutions and machine-learning/data-science projects:
https://github.com/JBielan

May the code be with you!
"""