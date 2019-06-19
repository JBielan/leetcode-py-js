class Solution(object):
    def duplicateZeros(self, arr):
        i = 0       # it's better to start from the beginning as last elements will be removed
        while i < len(arr):     # while is better as the list will be modified
            if arr[i] == 0:     # when element is 0
                arr.insert(i, 0)        # insert 0 along to it
                arr.pop(-1)     # remove last element
                i += 1      # go to the next element - after adding index has to be increased by 2
            i += 1      # check next element