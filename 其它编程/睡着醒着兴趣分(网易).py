import sys
if __name__ == "__main__":
    while True:
        line1 = sys.stdin.readline().strip()
        if line1 == '':
            break
        line2 = sys.stdin.readline().strip()
        if line2 == '':
            break
        line3 = sys.stdin.readline().strip()
        if line3 == '':
            break
        line1 = [int(i) for i in line1.split()]   # 两个数：一共几分钟，每次叫醒能够维持几分钟
        line2 = [int(i) for i in line2.split()]   # 对每分钟的兴趣得分
        line3 = [int(i) for i in line3.split()]
        k = line3    # 每分钟是醒着还是睡着
        total = []
        for i in range(line1[0]):    # 循环每个分钟，假设该分钟叫醒
            sum = 0
            line3 = [_ for _ in k]
            if i + line1[1] <= line1[0]:
                line3[i:i+line1[1]] = [1] * line1[1]
            else:
                line3[i:] = [1] * (line1[0] - i)    # 后面所有时间都醒着
            for j in range(line1[0]):
                sum += (line2[j] * line3[j])
            total.append(sum)
        print(max(total))

# 输入
# 6 3
# 1 3 5 2 5 4
# 1 1 0 1 0 0
# 输出
# 16
