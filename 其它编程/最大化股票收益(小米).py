# -*- coding: utf-8 -*-
# @Author: LiLing
# @Date:   2018-09-13 17:18:44
# @Last Modified by:   Liling
# @Last Modified time: 2018-09-13 18:08:54
"""
风口之下，猪都能飞。当今中国股市牛市，真可谓“错过等七年”。 给你一个回顾历史的机会，已知一支股票连续n天的价格走势，
以长度为n的整数数组表示，数组中第i个元素（prices[i]）代表该股票第i天的股价。 假设你一开始没有股票，但有至多两次买入1股而后
卖出1股的机会，并且买入前一定要先保证手上没有股票。若两次交易机会都放弃，收益为0。 设计算法，计算你能获得的最大收益。 
输入数值范围：2<=n<=100,0<=prices[i]<=100
示例1
输入
3,8,5,1,7,8
输出
12
"""
"""
解法一
DP，把问题按天分解，用四个变量分别记录截至这天的，第一次买的最高收益，第一次卖出的最高收益，第二次买的最高收益，
第二次卖出的最高收益。所以循环结束得到的就是第二次卖出的最高收益

firstBuy表示第一次买入的最大收益，因为是买入所以是负值；
firstSell表示第一次卖出的最大收益；
secondBuy表示第二次买入的最大收益；
secondSell表示第二次卖出的最大收益；
参考：https://discuss.leetcode.com/topic/32288/2ms-java-dp-solution/2
时间复杂度O(n), 空间复杂度O(1)
似乎有问题？不满足在第二次买之前一定卖掉？
"""
def calculateMax(prices):
	firstBuy = -float('Inf')
	firstSell = 0
	secondBuy = -float('Inf')
	secondSell = 0

	for curp in prices:
		firstBuy = max(firstBuy, -curp)
		firstSell = max(firstSell, firstBuy+curp)
		secondBuy = max(secondBuy, firstSell-curp)
		secondSell = max(secondSell, secondBuy+curp)

	return secondSell

print(calculateMax([3,8,5,1,9,8]))

"""
解法二
两次买卖机会，则一次出现在左边，一次出现在右边，利用动态规划的思想，首先从最左边开始从左往右扫描，求出最大收益，
然后从最右边开始从右往左扫描求出右边的最大收益，然后再比较一次和的大小，就可以得出。
"""
def calculateMax(prices):
	n = len(prices)
	if n<=1:
		return 0
	left = [0]*n
	right = [0]*n
	min = prices[0]
	for i in range(1,n):
		if prices[i] > prices[i-1]:
			left[i] = max(prices[i]-min, left[i-1])
		else:
			left[i] = left[i-1]
			if prices[i] < min:
				min = prices[i]

	high = prices[n-1]
	for i in range(n-2,-1,-1):
		if prices[i] < prices[i+1]:
			right[i] = max(high-prices[i], right[i+1])
		else:
			right[i] = right[i-1]
			if prices[i]>high:
				high = prices[i]

	result = 0
	for i in range(n):
		result = max(result, right[i]+left[i])

	return result

print(calculateMax([3,8,5,1,9,8]))