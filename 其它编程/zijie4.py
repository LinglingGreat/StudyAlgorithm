import sys
n = int(sys.stdin.readline().strip())
ans = []
for i in range(n):
    ans.append(int(sys.stdin.readline().strip()))
def fmax(numlist):
    if len(numlist) == 1:
        return numlist[0]
    i = 0
    resmax = 0
    while i < len(numlist):
        res = numlist[i]
        res *= (numlist[i-1] if i>0 else 1)
        res *= (numlist[i+1] if i+1<len(numlist) else 1)
        res += fmax(numlist[:i]+numlist[i+1:])
        resmax = max(resmax, res)
        i += 1
    return resmax

print(fmax(ans))