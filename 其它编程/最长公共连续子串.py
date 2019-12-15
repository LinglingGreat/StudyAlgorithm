# -*- coding: utf-8 -*-
"""
大给出两个字符串（可能包含空格）,找出其中最长的公共连续子串,输出其长度。
输入描述:
输入为两行字符串（可能包含空格），长度均小于等于50.
输出描述:
输出为一个整数，表示最长公共连续子串的长度。
输入例子1:
abcde
abgde
输出例子1:
2
"""
"""
DP问题，利用空间换时间，时间复杂度O(NM),空间O(NM)
思想：
创建一张二维表，本来这张表是用来存储字符A[i]和B[j]是否相等然后将表中(i,j)位置置为1。
遍历结束后，计算所有的对角线上连续1的个数，取最大值就是结果。但是现在，换种方法，
遍历的同时，计算当前斜对角的值，然后用一个变量res记录最大的值即可。
它的公式为：如果A[i - 1] == B[j - 1]，那么dp[i][j] = dp[i - 1][j - 1] + 1;
其中dp[0][...]和dp[...][0]都是0，这是初始状态。
"""
A = input()
B = input()


def longest_common_substring(A, B):
    m = len(A)
    n = len(B)
    if m == 0 or n == 0:
        return 0
    mat = list([0] * n for i in range(m))
    max_length = 0
    for i in range(m):
        for j in range(n):
            if A[i] == B[j]:
                if i == 0 or j == 0:
                    mat[i][j] = 1
                else:
                    mat[i][j] = mat[i - 1][j - 1] + 1
                max_length = max(max_length, mat[i][j])
    return max_length


print(longest_common_substring(A, B))

