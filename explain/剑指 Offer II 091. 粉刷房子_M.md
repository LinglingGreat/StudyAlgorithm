#### [剑指 Offer II 091. 粉刷房子](https://leetcode-cn.com/problems/JEj789/)

难度：中等

标签：[数组](../原理/数组.md)，[动态规划](../原理/动态规划.md)

相同题目：[256. 粉刷房子](https://leetcode-cn.com/problems/paint-house)

假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的正整数矩阵 costs 来表示的。

例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。

请计算出粉刷完所有房子最少的花费成本。

 

示例 1：

输入: costs = [[17,2,17],[16,16,5],[14,3,19]]
输出: 10
解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
     最少花费: 2 + 5 + 3 = 10。
示例 2：

输入: costs = [[7,6,2]]
输出: 2


提示:

costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20

用动态规划解决问题的关键在于找出状态转移方程。根据粉刷的规则，相邻的两幢房子不能被粉刷成相同的颜色，要计算粉刷到标号为i的房子时的成本，还需要考虑标号为i-1的房子的颜色。因此，需要3个表达式，即r（i）、g（i）、b（i），分别表示将标号为i的房子粉刷成红色、绿色和蓝色时粉刷标号从0到i的i+1幢房子的最少成本。假设粉刷每幢房子的成本用一个二维数组costs表示，那么costs[i]中包含的3个数字分别是将标号为i的房子粉刷成红色、绿色和蓝色的成本。当标号为i的房子被粉刷成红色时，标号为i-1的房子可以被粉刷成绿色或蓝色，因此r（i）=min（g（i-1），b（i-1））+costs[i][0]。类似地，当标号为i的房子被粉刷成绿色时，标号为i-1的房子可以被粉刷成红色或蓝色，因此g（i）=min（r（i-1），b（i-1））+costs[i][1]；当标号为i的房子被粉刷成蓝色时，标号为i-1的房子可以被粉刷成红色或绿色，因此b（i）=min（r（i-1），g（i-1））+costs[i][2]。



二维空间

```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0 for _ in range(3)] for _ in range(n + 1)]
        for i in range(n):
            dp[i + 1][0] = min(dp[i][1], dp[i][2]) + costs[i][0]
            dp[i + 1][1] = min(dp[i][0], dp[i][2]) + costs[i][1]
            dp[i + 1][2] = min(dp[i][0], dp[i][1]) + costs[i][2]
        
        return min(dp[n])
```

优化空间

```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        a0 = costs[0][0]
        a1 = costs[0][1]
        a2 = costs[0][2]
        
        for i in range(1, n):
            b0 = min(a1, a2) + costs[i][0]
            b1 = min(a0, a2) + costs[i][1]
            b2 = min(a0, a1) + costs[i][2]
            a0, a1, a2 = b0, b1, b2
            
        return min(a0, a1, a2)

作者：Hanxin_Hanxin
链接：https://leetcode-cn.com/problems/JEj789/solution/cpython3java-1er-wei-dp-by-hanxin_hanxin-suxa/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

