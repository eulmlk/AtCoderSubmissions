from collections import defaultdict, deque, Counter
from math import gcd, lcm, sqrt, ceil, floor
from heapq import heapify, heappop, heappush
from sys import stdin


def input():
    return stdin.readline().strip()


def readList():
    return list(map(int, input().split()))


def solve():
    n, cap = readList()
    weights, values = [], []

    for _ in range(n):
        w, v = readList()
        weights.append(w)
        values.append(v)

    memo = {}

    def knapsack(ind, cur):
        if ind == n:
            return 0

        state = (ind, cur)
        if state not in memo:
            include = 0
            if weights[ind] <= cur:
                include = values[ind] + knapsack(ind + 1, cur - weights[ind])

            exclude = knapsack(ind + 1, cur)
            memo[state] = max(include, exclude)

        return memo[state]

    print(knapsack(0, cap))


t = 1

for _ in range(t):
    solve()
