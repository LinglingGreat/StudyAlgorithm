'''
===========================================
  @author:  jiaxin         
  @time:    2018/7/22 0022   21:08 
===========================================
'''
print('输入范例：')
n = int(input())
m = int(input())
n_shape = input()
map = []    # 邻接矩阵
for i in range(n):
    line = [int(x) for x in input().split()]
    map.append(list(line))
# n, m = 3, 2
# map = [[0, 2, 3], [2, 0, 1], [3, 1, 0]]
# n, m = 4, 3
# map = [[0, 2, 4, 3], [2, 0, 5, 3], [4, 5, 0, 4], [3, 3, 4, 0]]
res = [([float('inf')]*n)for _ in range(n)]   # 最短路径矩阵
 
 
def mypath(n, m, distance):
    if m == 0:    # 路径长度为0,已经走到终点了，更新最短路径
        if res[source][n] > distance:
            res[source][n] = distance
            return
        return
    info = map[n]
    for i, j in enumerate(info):
        if j != 0:   # j是n到i这条边的"代价"
            mypath(i, m-1, distance + j)
    return
 
 
for i in range(n):
    source = i
    mypath(i, m, 0)
 
print('输出范例：')
for i in res:
    print(i)

# 输入范例：
# 3
# 2
# 3 3
# 0 2 3
# 2 0 1
# 3 1 0
# 输出范例：
# [4, 4, 3]
# [4, 2, 5]
# [3, 5, 2]
