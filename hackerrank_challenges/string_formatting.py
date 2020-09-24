"""
https://www.hackerrank.com/challenges/python-string-formatting/problem
> Problem
Given an integer n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

The four values must be printed on a single line in the order specified above for each
i from 1 to n. Each value should be space-padded to match the width of the binary value of n.

> Input Format
A single integer denoting n.

> Constraints
1 <= n <= 99

> Output Format
Print n lines where each line i (in the range 1 <= i <= n) contains the respective decimal, octal, capitalized
hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.

> Sample Input

17

> Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""


def print_formatted(number):
    m = number
    w = 0
    while m > 0:
        m //= 2
        w += 1
    fom = "{0:" + str(w) + "d} " + "{0:" + str(w) + "o} " + "{0:" + str(w) + "X} " + "{0:" + str(w) + "b} "

    for i in range(1, n + 1):
        print(fom.format(i))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
