# 有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，
# 5，7，9，15，21。 
# 
#  示例 1: 
# 
#  输入: k = 5
# 
# 输出: 9
#  
#  Related Topics 堆 队列 数学 
#  👍 50 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        numList = [0] * (k+1)
        p3 = 0
        p5 = 0
        p7 = 0
        numList[0] = 1
        for i in range(1, k):
            numList[i]=min(numList[p3] * 3, numList[p5] * 5, numList[p7] * 7)
            if numList[i] == numList[p3] * 3:
                p3 += 1
            if numList[i] == numList[p5] * 5:
                p5 += 1
            if numList[i] == numList[p7] * 7:
                p7 += 1
        return numList[k - 1]
# leetcode submit region end(Prohibit modification and deletion)
