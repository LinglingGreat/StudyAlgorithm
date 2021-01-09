#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

# @lc code=start
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # 一行代码大佬
        # return reduce(lambda x, y: x&y, map(Counter, A)).elements()
        str_dict = {}
        str_dict_tmp = {}
        for i in A[0]:
            str_dict[i] = str_dict.get(i, 0) + 1
        for i in A[1:]:
            for j in i:
                str_dict_tmp[j] = str_dict_tmp.get(j, 0) + 1
            for k, v in str_dict.items():
                str_dict[k] = min(v, str_dict_tmp.get(k, 0))
            str_dict_tmp = {}
        reslist = []
        for k, v in str_dict.items():
            if v>=1:
                reslist.extend([k]*v)
        return reslist




        
# @lc code=end

