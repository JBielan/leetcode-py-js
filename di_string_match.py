class Solution:
    def diStringMatch(self, S):
        result = []         # we'll store result list here
        maximum = len(S)    # maximum number in permuatations list
        minimum = 0         # minimum number in permuatations list
        for s in S:
            if s =='I':
                result.append(minimum)  # if next should be higher, take the smallest left number and add to the result
                minimum += 1            # right now minimum is bigger by 1
            else:
                result.append(maximum)  # if next should be lower, take the biggest left number and add to the result
                maximum -= 1            # right now maximum is smaller by 1
        result.append(maximum)          # just add last number in the end - can be result.append(minimum) as well
        return result
'''
This way you don't have to iterate through all permuations and still you'll get the right list in the end.
'''