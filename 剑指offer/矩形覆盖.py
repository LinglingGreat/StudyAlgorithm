'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
'''
依旧是斐波那契数列
target=n
第一次摆放一块 2*1 的小矩阵，则摆放方法总共为f(target-1)
第一次摆放一块1*2的小矩阵，则摆放方法总共为f(target-2)
'''

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number < 1:
            return 0
        a, b = 1, 1
        if number >= 2:
            for i in range(2,number+1):
                a, b = b, a+b
        return b

test = Solution()
print(test.rectCover(100))