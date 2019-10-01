import math
import itertools


class Solution:
    def largestTriangleArea(self, points):
        def calc_area(a, b, c):     # this is just a formula for triangle area
            s = (a + b + c) / 2
            return math.sqrt((s*(s - a) * (s - b) * (s - c)))

        def distance(a, b):     # formula to calculate distance (right triangle - pythagoras)
            return math.sqrt((a[0]-b[0])**2 + (a[1] - b[1])**2)


        combos = list(itertools.combinations(points, 3))        # all possibilities of triples
        best = 0

        for i in range(len(combos)):        # for every possibility calculate 3 lengths
            a = distance(combos[i][0], combos[i][1])
            b = distance(combos[i][0], combos[i][2])
            c = distance(combos[i][1], combos[i][2])

            sides = [a, b, c]
            sides.sort()
            if sides[0] + sides[1] > sides[2]:      # if sides can form a triangle
                area = calc_area(a, b, c)       # calculate the area
                if area > best:
                    best = area     # if it's bigger than best, replace it with new value

        return best     # when all possibilities will be checked, return the biggest area


solution = Solution()
print(solution.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))