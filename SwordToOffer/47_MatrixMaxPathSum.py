# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode47: 矩阵最大路径和问题或者说礼物最大价值问题

#data中的数字都是大于0的
def MatrixMaxPathSum(data):
    nrow, ncol = len(data), 0
    if nrow:
        ncol = len(data[0])
    res = [0]*ncol
    for i in range(nrow):
        for j in range(ncol):
            if i == 0 and j == 0:
                res[j] = data[i][j]
            elif i == 0:
                res[j] = res[j-1] + data[i][j]
            elif j == 0:
                res[j] = res[j] + data[i][j]
            else:
                res[j] = max(res[j-1], res[j]) + data[i][j]
    if res:
        return res[-1]
    return None

if __name__ == "__main__":
    data = [[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]
    data = [[5]]
    for row in data:
        print(row)
    print(MatrixMaxPathSum(data))
