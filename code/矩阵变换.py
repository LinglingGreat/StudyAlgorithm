# [
#     [1, 2, 3, 4],
#     [2, 3, 4, 5],
#     [3, 4, 5, 6],
#     [4, 5, 6, 7]
# ]

# [
#     [1, 2, 3, 4],
#     [2, 12, 16, 5],
#     [3, 16, 20, 6],
#     [4, 5, 6, 7]
# ]

# 原地修改，每次保存前一行以及当前行前一列的数据
import copy
def func(input_matrix):
    rows = len(input_matrix)
    cols = len(input_matrix[0])
    output_matrix = copy.deepcopy(input_matrix)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # if 0 < i < rows and 0 < j < cols:
            output_matrix[i][j] = input_matrix[i-1][j] + input_matrix[i][j-1]
            +input_matrix[i+1][j]+input_matrix[i][j+1]
    return output_matrix

if __name__ == "__main__":
    input_matrix = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7]]
    print(func(input_matrix))

