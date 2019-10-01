def numJewelsInStones(self, J: str, S: str) -> int:
    counter = 0
    for diamond in J:  # Pythonic way to iterate through a list
        for stone in S:
            if stone == diamond:
                counter += 1  # Add 1 when stone is a diamond
    return counter

"""
I hope I helped you in some way. If you like this solution, I'll be very happy if you click "Star" on Github:
https://github.com/JBielan/leetcode-python

As well feel free to follow my account for daily coding solutions and machine-learning/data-science projects:
https://github.com/JBielan

May the code be with you!
"""