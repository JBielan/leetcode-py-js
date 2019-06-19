class Solution:
    def sumEvenAfterQueries(self, A, queries):

        even_sum = sum(i for i in A if i % 2 == 0)  # sum of even numbers is calculated only once!
        even_sums = []

        for val, index in queries:
            if A[index] % 2 == 0: even_sum -= A[
                index]  # to keep the sum right - old value has to be subtract and new value added which gives the difference
            A[index] += val  # required change comes here
            if A[index] % 2 == 0: even_sum += A[index]  # here value is added to achieve the difference
            even_sums.append(even_sum)  # when the difference is achieved just add total sum to the list

        return even_sums  # return the result after the loop

    '''
    This way to calculate the sum it's not necessary to iterate over the list all the time. It's enough to just correct previous result according to the new number.
    '''