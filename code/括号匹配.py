# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
# 示例
# 示例 1:
# 输入: "()"
# 输出: true
# 示例 2:
# 输入: "()[]{}"
# 输出: true
# 示例 3:
# 输入: "(]"
# 输出: false
# 示例 4:
# 输入: "([)]"
# 输出: false
# 示例 5:
# 输入: "{[]}"
# 输出: true￼
def func(inputstr):
    if inputstr == "":
        return True
    stack = []
    dic = {")": "(", "]": "[", "}": "{"}
    for i in inputstr:
        if i in ["(", "[", "{"]:
            stack.append(i)
        elif i in dic:
            left = stack.pop()
            if left != dic[i]:
                return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    print(func("()"))
    print(func("()[]{}"))
    print(func("([)]"))