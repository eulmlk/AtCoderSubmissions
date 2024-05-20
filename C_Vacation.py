from collections import defaultdict, deque, Counter
from math import gcd, lcm, sqrt, ceil, floor
from heapq import heapify, heappop, heappush
from sys import stdin


def input():
    return stdin.readline().strip()


def readList():
    return list(map(int, input().split()))


def solve():
    n = int(input())
    bestA = bestB = bestC = 0

    for _ in range(n):
        a, b, c = readList()

        a += max(bestB, bestC)
        b += max(bestA, bestC)
        c += max(bestA, bestB)

        bestA = a
        bestB = b
        bestC = c

    print(max(bestA, bestB, bestC))


t = 1

for _ in range(t):
    solve()
