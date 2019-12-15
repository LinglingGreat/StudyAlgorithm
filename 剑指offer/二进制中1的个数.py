'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
'''
如果一个整数不为0，那么这个整数至少有一位是1。如果我们把这个整数减1，那么原来处在整数最右边的1就会变为0，
原来在1后面的所有的0都会变成1(如果最右边的1后面还有0的话)。其余所有位将不会受到影响。
举个例子：一个二进制数1100，从右边数起第三位是处于最右边的一个1。减去1后，第三位变成0，它后面的两位0变成了1，而前面的1保持不变，
因此得到的结果是1011.我们发现减1的结果是把最右边的一个1开始的所有位都取反了。这个时候如果我们再把原来的整数和减去1之后的结果做与运算，
从原来整数最右边一个1那一位开始所有位都会变成0。如1100&1011=1000.也就是说，把一个整数减去1，再和原整数做与运算，
会把该整数最右边一个1变成0.那么一个整数的二进制有多少个1，就可以进行多少次这样的操作。
'''

class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n-1)&n
        return count

    def NumberOf2(self, n):
        if n < 0:
            s = bin(n & 0xffffffff)
        else:
            s = bin(n)
        return s.count('1')

    # 判断一个数是不是2得整数次幂
    def powerOf2(self, n):
        if n&(n-1) == 0:
            return True
        else:
            return False
    # 判断两个数的二进制表示有多少位不一样, 直接比较两个数的二进制异或就可以
    def andOr(self, m, n):
        diff = m^n
        count = 0
        while diff:
            count += 1
            diff = diff&(diff-1)
        return count

S = Solution()
print(S.NumberOf1(-1))
print(S.NumberOf2(-1))
print(S.powerOf2(64))
print(S.powerOf2(63))
print(S.andOr(10, 13))