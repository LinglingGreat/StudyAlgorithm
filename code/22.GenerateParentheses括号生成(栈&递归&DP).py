'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''
'''
方法一：暴力法
思路
我们可以生成所有 2^{2n}个 '(' 和 ')' 字符构成的序列。然后，我们将检查每一个是否有效。
算法
为了生成所有序列，我们使用递归。长度为 n 的序列就是 '(' 加上所有长度为 n-1 的序列，以及 ')' 加上所有长度为 n-1 的序列。
为了检查序列是否为有效的，我们会跟踪平衡，也就是左括号的数量减去右括号的数量的净值。如果这个值始终小于零或者不以零结束，该序列就是无效的，否则它是有效的。
时间复杂度：O(2^{2n}n)，对于 2^{2n}个序列中的每一个，我们用于建立和验证该序列的复杂度为 O(n)。
空间复杂度：O(2^{2n}n)，简单地，每个序列都视作是有效的。请参见方法三以获得更严格的渐近界限。
'''
class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

'''
方法二：回溯法
思路和算法

只有在我们知道序列仍然保持有效时才添加 '(' or ')'，而不是像方法一那样每次添加。我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，

如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。
'''
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

'''
方法三：闭合数
思路
为了枚举某些内容，我们通常希望将其表示为更容易计算的不相交子集的总和。
考虑有效括号序列 S 的闭包数：至少存在index> = 0，使得 S[0], S[1], ..., S[2*index+1]是有效的。 显然，每个括号序列都有一个唯一的闭包号。 我们可以尝试单独列举它们。
算法
对于每个闭合数 c，我们知道起始和结束括号必定位于索引 0 和 2*c + 1。然后两者间的 2*c 个元素一定是有效序列，其余元素一定是有效序列。
方法二与方法三的复杂度类似
'''
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
'''
方法四
To generate all n-pair parentheses, we can do the following:
Generate one pair: ()
Generate 0 pair inside, n - 1 afterward: () (...)...
Generate 1 pair inside, n - 2 afterward: (()) (...)...
...
Generate n - 1 pair inside, 0 afterward: ((...))
I bet you see the overlapping subproblems here. Here is the code:
(you could see in the code that x represents one j-pair solution and y represents one (i - j - 1) pair solution, 
and we are taking into account all possible of combinations of them)
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]