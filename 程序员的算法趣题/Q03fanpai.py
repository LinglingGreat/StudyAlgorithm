
# 对于每一张牌，将其未来将会发生的翻转操作一次性完成
for i in range(1, 101):
    flag = False
    # 寻找这张牌的所有约数，即每一次翻转的情形
    for j in range(1, i+1):
        if i % j == 0:
            flag = not flag  # 相当于一次翻牌
    if flag:
        print(i)

