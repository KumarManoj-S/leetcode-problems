class Solution:
    def mincostTickets(self, days, costs) -> int:
        hmap = {}

        def find_costs(d, c, i=0):
            if i in hmap: return hmap[i]
            if i >= len(d): return 0

            results = []
            for idx, no_of_days in enumerate([1, 7, 30]):
                j = i
                while j < len(d) and d[j] < d[i] + no_of_days:
                    j += 1
                results.append(c[idx] + find_costs(d, c, j))

            cost = min(results)
            hmap[i] = cost

            return cost

        return find_costs(days, costs)

