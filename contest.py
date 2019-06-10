class Solution:
    def assignBikes(self, workers, bikes) -> int:
        def permutations(iterable, r=None):
            # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
            # permutations(range(3)) --> 012 021 102 120 201 210
            pool = tuple(iterable)
            n = len(pool)
            r = n if r is None else r
            if r > n:
                return
            indices = list(range(n))
            cycles = list(range(n, n - r, -1))
            yield tuple(pool[i] for i in indices[:r])
            while n:
                for i in reversed(range(r)):
                    cycles[i] -= 1
                    if cycles[i] == 0:
                        indices[i:] = indices[i + 1:] + indices[i:i + 1]
                        cycles[i] = n - i
                    else:
                        j = cycles[i]
                        indices[i], indices[-j] = indices[-j], indices[i]
                        yield tuple(pool[i] for i in indices[:r])
                        break
                else:
                    return

        workers_dic = {}
        for i, worker in enumerate(workers):
            workers_dic[i] = []
            for bike in bikes:
                workers_dic[i].append(abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]))

        options = []
        for x in permutations(range(len(workers_dic[0])), len(workers_dic)):
            options.append(x)

        best = 999999999

        for option in options:
            current = 0
            for i in range(len(option)):
                current += workers_dic[i][option[i]]

            if current < best:
                best = current

        return best

workers = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]
bikes = [[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999],[7,999],[8,999]]

sol = Solution()
print(sol.assignBikes(workers, bikes))