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
    arr = readList()
    result = [0] * n
    result[n - 2] = abs(arr[n - 1] - arr[n - 2])

    for i in range(n - 3, -1, -1):
        jump1 = result[i + 1] + abs(arr[i] - arr[i + 1])
        jump2 = result[i + 2] + abs(arr[i] - arr[i + 2])
        result[i] = min(jump1, jump2)

    print(result[0])


t = 1

for _ in range(t):
    solve()
