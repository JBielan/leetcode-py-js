class Solution:
    def numUniqueEmails(self, emails) -> int:
        distinct_emails = []                                # addresses will be stored here
        for mail in emails:                                 # for every single mail
            splitted = mail.split('@')                      # split local and domain part
            splitted[0] = splitted[0].replace('.', '')      # remove dots from the local part

            idx = splitted[0].find('+')                     # find "+", -1 is returned when there isn't any "+"
            if idx != -1:
                splitted[0] = splitted[0][:idx]             # cut "+" and everything afterward for local part

            # full_email = '@'.join(splitted)               # unnecessary step as we care only about amount

            if splitted not in distinct_emails:             # add to the list only if there isn't the same email
                distinct_emails.append(splitted)

        return len(distinct_emails)                         # return length of the list

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

As well feel free to follow my account for daily coding solutions and machine-learning/data-science projects:
https://github.com/JBielan

May the code be with you!
"""