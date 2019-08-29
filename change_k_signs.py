class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        """
        The idea is to start with the smallest items as it's possible to increase the sum only changing negative numbers.
        After sorting an array, if the number is negative, change its sign and less 1 from K.
        If next non negative number is zero, just return sum because you can change zero's sign and there are only positive numbers left.
        If the number is positive the best scenario is to not change anything. In case of even K just return the sum.
        In case of negative K check whether it's better to change the sign of first positive number or last negative that became positive.
        Change that number and return the sum.
        Remember to return the array also when while loop is escaped.
        """
        A = sorted(A)
        i = 0
        while i < len(A) and K > 0:
            if A[i] < 0:
                A[i] = -A[i]
                K -= 1
            elif A[i] == 0:
                return sum(A)
            else:
                if K % 2 == 0:
                    return sum(A)
                else:
                    if A[i] < A[i - 1]:
                        A[i] = -A[i]
                        return sum(A)
                    else:
                        print(A)
                        A[i - 1] = -A[i - 1]
                        return sum(A)
            i += 1

        return sum(A)
