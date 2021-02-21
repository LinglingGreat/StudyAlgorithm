# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。 
# 
#  示例： 
# 
#  输入： arr = [1,3,5,7,2,4,6,8], k = 4
# 输出： [1,2,3,4]
#  
# 
#  提示： 
# 
#  
#  0 <= len(arr) <= 100000 
#  0 <= k <= min(100000, len(arr)) 
#  
#  Related Topics 堆 排序 分治算法 
#  👍 38 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        def partition(left, right):
            pivot = left
            lt = left + 1
            gt = right
            while True:
                while lt <= right and arr[lt] < arr[pivot]:
                    lt += 1
                while gt >= left and arr[gt] > arr[pivot]:
                    gt -= 1
                if lt > gt:
                    break;
                arr[lt], arr[gt] = arr[gt], arr[lt]
                lt += 1
                gt -= 1
            arr[pivot], arr[gt] = arr[gt], arr[pivot]
            return gt

        # 边界条件
        if k >= len(arr):
            return arr
        elif k <= 0:
            return []

        left, right = 0, len(arr) - 1
        while True:
            # 基准点左边的数字的值都小于基准点，右边的都大于基准点
            pivot = partition(left, right)
            if pivot == k:
                break
            elif pivot > k:
                right = pivot - 1
            else:
                left = pivot + 1

        return arr[:k]

# leetcode submit region end(Prohibit modification and deletion)
