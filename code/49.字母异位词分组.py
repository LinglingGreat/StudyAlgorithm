#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """用字典存放，键是字符串排序后的tuple（键必须是不可变的，所以不能用列表），值是字符串组成的列表"""
        dic = {}
        for s in strs:
            sorts = tuple(sorted(s))
            if sorts in dic:
                dic[sorts].append(s)
            else:
                dic[sorts] = [s]
        return list(dic.values())

# @lc code=end

