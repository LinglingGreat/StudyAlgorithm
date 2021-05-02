# 请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(
# 1)。 示例： MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0);
#  minStack.push(-3); minStack.getMin();   --> 返回 -3. minStack.pop(); minStack.top
# ();      --> 返回 0. minStack.getMin();   --> 返回 -2. Related Topics 栈 
#  👍 45 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minval = float('inf')

    def push(self, x: int) -> None:
        # 如果遇到一个更小的值，把上一步的最小值存起来
        if x <= self.minval:
            if len(self.stack):
                self.stack.append(self.minval)
            self.minval = x
        self.stack.append(x)

    def pop(self) -> None:
        if not len(self.stack):
            return
        if len(self.stack) == 1:
            self.minval = float('inf')
        # 如果pop的是最小值，那么pop之后的元素就是下一个最小值。
        elif self.stack[-1] == self.minval:
            self.stack.pop()
            self.minval = self.stack[-1]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
