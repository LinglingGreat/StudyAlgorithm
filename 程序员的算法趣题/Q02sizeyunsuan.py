
op = ["+", "-", "*", "/", ""]
# 可以将上述运算符改为
# op = ["*", ""]
# 因为很容易发现，一旦用了'*'以外的任意运算符，最终的结果就凑不够4位数了
for num in range(1000, 10000):
    # 排除末尾数字为0的情况
    if num % 10 == 0:
        continue
    numlist = list(str(num))
    for op1 in op:
        for op2 in op:
            for op3 in op:
                # 排除对0开头的数字进行运算的情况，比如1*01等
                if (op1 != '' and numlist[1] == '0') or (op2 != '' and numlist[2] == '0'):
                    continue
                val = numlist[0] + op1 + numlist[1] + op2 + numlist[2] + op3 + numlist[3]
                if len(val) > 4:  # 至少插入一个运算符
                    if int(str(num)[::-1]) == eval(val):    # 如果逆序排序的数字与运算后的结果相等
                        print(str(num)+" ---> "+val+"="+str(num)[::-1])

