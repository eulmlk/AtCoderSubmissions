from collections import defaultdict, deque, Counter
from math import gcd, lcm, sqrt, ceil, floor
from heapq import heapify, heappop, heappush
from sys import stdin


def input():
    return stdin.readline().strip()


def readList():
    return list(map(int, input().split()))


def solve():
    s = input() + '$'
    t = input() + '$'
    n, m = len(s), len(t)

    result = [[0] * m for _ in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            if s[i] == t[j]:
                result[i][j] = 1 + result[i + 1][j + 1]
            else:
                result[i][j] = max(result[i][j + 1], result[i + 1][j])

    k = result[0][0]
    i, j = 0, 0
    common = []

    while len(common) < k:
        if s[i] == t[j]:
            common.append(s[i])
            i += 1
            j += 1
        elif result[i + 1][j] > result[i][j + 1]:
            i += 1
        else:
            j += 1

    print(''.join(common))


t = 1

for _ in range(t):
    solve()
