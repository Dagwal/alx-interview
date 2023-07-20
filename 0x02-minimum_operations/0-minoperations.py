#!/usr/bin/python3
""" a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file. """


def minOperations(n: int) -> int:
    """
    write a method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Argument:
    n: integer
    """
    if n <= 1:
        return 0
    if n <= 5:
        return n
    for i in range(n//2, -1, -1):
        if n % i == 0:
            return minOperations(i) + (n // i)

if __name__ == "__main__":
    minOperations()

    # iteration method
    # count = 0
    # for i in range(2, n + 1):
    #     # check if problem can be broken into smaller problem
    #     while not n % i:
    #         # if yes then add no of smaller problems to result.
    #         count += i
    #         # create smaller problem
    #         n /= i
    # return count

    # 1. We can find some largest number where n % k = 0.
    # 2. Then find # of steps(copy+pastes) to reach k
    # 3. Find number of pastes to reach n
    # 4. answer = #2 + #3
