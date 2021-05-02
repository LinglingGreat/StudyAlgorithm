def isHuiwen(number):
    dec_num = str(number)
    # python将十进制数转为二进制或八进制数时会带有前缀0b, 0o，所以要将前缀去掉
    bin_num = str(bin(number))[2:]
    oct_num = str(oct(number))[2:]
    # 要获得字符串s的逆序可用s[::-1]
    # 如果三个条件都满足，则返回True,否则返回False
    return dec_num == dec_num[::-1] and bin_num == bin_num[::-1] and oct_num == oct_num[::-1]


num = 11
while True:
    # 调用函数判断num是否是回文数，如果是，则输出该数，并停止循环
    if isHuiwen(num):
        print(num)
        break
    num += 2
