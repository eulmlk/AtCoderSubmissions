from collections import defaultdict, deque, Counter
from math import gcd, lcm, sqrt, ceil, floor
from heapq import heapify, heappop, heappush
from sys import stdin


def input():
    return stdin.readline().strip()


def readList():
    return list(map(int, input().split()))


def solve():
    n, k = readList()
    arr = readList()
    result = [0] * n
    k = min(k, n)

    for i in range(n - 2, -1, -1):
        minJump = float('inf')

        for j in range(1, k + 1):
            ind = i + j
            if ind >= n:
                break

            jump = result[ind] + abs(arr[i] - arr[ind])
            minJump = min(minJump, jump)

        result[i] = minJump

    print(result[0])


t = 1

for _ in range(t):
    solve()
