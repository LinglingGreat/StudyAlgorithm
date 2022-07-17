
#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    a = sys.stdin.readline().strip().split()
    n, k = int(a[0]), int(a[1])
    print(n, k)
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    score = list(map(int, line.split()))

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    wake = list(map(int, line.split()))

    ans = 0
    for i in range(len(wake)):
        if wake[i] == 1:
            ans += score[i]
    maxs = 0
    print(ans)
    for i in range(len(score)-2):
        maxscore = ans + (score[i] if wake[i]==0 else 0) +(score[i+1] if wake[i+1]==0 else 0) +(score[i+2] if wake[i+2]==0 else 0)
        print(maxscore)
        if maxscore > maxs:
            maxs = maxscore

    print(maxs)