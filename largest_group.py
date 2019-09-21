class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        """ 1 iteration is needed to solve the problem """
        curr, n, start, res, l = None, 0, 0, [], len(S)
        # curr - current group character, n - number of group characters, start -initial idx for the group
        # res - list with results, l - length of string S

        for i in range(l):  # for every index in S string
            if S[i] == curr:  # if element is equal to group character
                n += 1  # add 1 to group quantity
                if i == l - 1 and n >= 3:  # scenario for strings ending with large group
                    res.append([start, i])
            else:  # if group ends
                if n >= 3:  # in case it was a large group
                    res.append([start, i - 1])  # add first and last index to result
                curr = S[i]  # set current character as current element
                start = i  # set new start index
                n = 1  # set quantity to 1
        return res  # when all elements pass, return result array
