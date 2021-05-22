# 给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。注意：n-m尽量最小，也就是说，找出符合条件的最短
# 序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。 
#  示例： 
#  输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
# 输出： [3,9]
#  
#  提示： 
#  
#  0 <= len(array) <= 1000000 
#  
#  Related Topics 排序 数组 
#  👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        if not array: return [-1, -1]
        last = -1
        first = -1
        maxv = -float('inf')
        minv = float('inf')
        n = len(array)
        for i in range(n):
            if array[i] < maxv:
                last = i
            else:
                maxv = max(maxv, array[i])
            if array[n - 1 - i] > minv:
                first = n - 1 - i
            else:
                minv = min(minv, array[n - 1 - i])
        return [first, last]
# leetcode submit region end(Prohibit modification and deletion)
