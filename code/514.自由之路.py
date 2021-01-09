#
# @lc app=leetcode.cn id=514 lang=python3
#
# [514] 自由之路
#

# @lc code=start
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        # 存放每个字符在ring中的出现位置
        posdict = dict()
        for i in range(n):
            if ring[i] not in posdict:
                posdict[ring[i]] = [i]
            else:
                posdict[ring[i]].append(i)
        # dp[i][j]表示拼写到key[i]且ring[j]在12点钟位置所需要的步数，初始化为无穷大
        dp = [[float('inf') for j in range(n)] for i in range(m)]
        # 初始化key的第一个字符的dp值，方便后续计算其它dp
        for j in posdict[key[0]]:
            dp[0][j] = min(j, n-j) + 1
        for i in range(1, m):   # 遍历key的每一个字符
            for j in posdict[key[i]]:   # 遍历这个字符在ring的所有位置
                for k in posdict[key[i-1]]:   # 遍历上一个字符在ring的所有位置
                    # 此时k在12点位置，顺时针数是j-k，逆时针数是n-(j-k),k可能比j大，所以计算绝对值
                    dp[i][j] = min(dp[i][j], dp[i-1][k]+min(abs(j-k), n-abs(j-k))+1)
        return min(dp[m-1])


        
# @lc code=end

