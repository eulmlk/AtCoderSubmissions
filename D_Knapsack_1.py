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

    vals = [[0] * (cap + 1) for _ in range(n)]
    for cur in range(weights[n - 1], cap + 1):
        vals[n - 1][cur] = values[n - 1]

    for i in range(n - 2, -1, -1):
        for cur in range(cap + 1):
            include = 0
            exclude = vals[i + 1][cur]
            if weights[i] <= cur:
                include = values[i] + vals[i + 1][cur - weights[i]]

            vals[i][cur] = max(include, exclude)

    print(vals[0][cap])


t = 1

for _ in range(t):
    solve()
