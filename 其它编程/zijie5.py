import sys
import math

def pem(n, m):
    if m == 0 or m == n:
        return 1
    return math.factorial(n)/(math.factorial(m)*math.factorial(n-m))


n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
ans = list(map(int, line.split()))
res = 2
for i in range(1, n-1):
    left = i
    right = n-i-1
    for j in range(1, left+1):
        res += pem(right+1, j)*pem(left-1, j-1)
print(int(res % 12345678))