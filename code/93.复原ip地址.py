#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        seg_count = 4
        ans = []
        segments = [0] * seg_count

        def dfs(segstart, segid):
            # 一种可能性已经遍历完
            if segid == seg_count:
                if segstart == len(s):
                    ans.append(".".join(str(i) for i in segments))
                return
            
            if segstart == len(s):
                return
                
            if s[segstart] == "0":
                segments[segid] = "0"
                dfs(segstart+1, segid+1)
            
            addr = 0
            for segend in range(segstart, len(s)):
                addr = addr * 10 + (ord(s[segend]) - ord("0"))
                if 0 < addr <= 255:
                    segments[segid] = addr
                    dfs(segend+1, segid+1)
                else:
                    break
        
        dfs(0, 0)
        return ans
# @lc code=end

