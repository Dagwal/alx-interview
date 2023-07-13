#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0

    min_ops = 0
    i = 2
    while i <= n:
        if n % i == 0:
            min_ops += i
            n = n / i
        else:
            i += 1
    return min_ops
