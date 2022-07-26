# 给定两个长度为 n ( 0 < n <= 8 ) 的数字串 (由 1 到 9 构成)，我们希望对第一个数字串做一系列如下操作：
#     1. 将数字串的某一位加 1
#     2. 将数字串的某一位减 1
#     3. 交换数字串中任意两个数字的位置
#     最终使得第一个数字串变成第二个数字串，请问最少需要多少次操作.
# 举例： 142 和 251，需要两次
str1 = '123'
str2 = '251'
list1 = list(str1)
list2 = list(str2)

same = [a for a in str1 if a in str2]
print(same)
diff = [a for a in str1 if a not in str2]

num = 0
add = []
sub = []
for d1, d2 in zip(list1, list2):
    n = abs(int(d1)-int(d2))
    num += n
    if d1>d2:
        sub.append(n)
    elif d2>d1:
        add.append(n)

add = sorted(add)
sub = sorted(sub)
for a, b in zip(add,sub):
    if a == b:
        num -= (int(a)+int(b)-1)

print(num)