### 233.数字1的个数

给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

**示例:**

```
输入: 13
输出: 6 
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
```

链接：

https://leetcode.com/problems/number-of-digit-one/

https://leetcode-cn.com/problems/number-of-digit-one/



参考解法：

https://leetcode.com/problems/number-of-digit-one/discuss/64382/JavaPython-one-pass-solution-easy-to-understand

计算每位(个位、百位、千位...)上1出现的次数。

假设n=xyzdabc

考虑千位上1出现的次数，那么：

```
(1) xyz * 1000                     if d == 0，此时xyz以及abc有这么多种可能(xyz的取值从000到xyz，abc的取值从000到999，下面同理)
(2) xyz * 1000 + abc + 1           if d == 1
(3) xyz * 1000 + 1000              if d > 1
```

统计出每一位上1出现的次数，加起来即可。