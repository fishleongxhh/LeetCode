# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解矩阵的最大和最小累积和路径问题

#矩阵形状为nrow*ncol
#从左上角到右下角，只能向右或者向下走，求最大累积和

def MaxPathSum(nums):
    nrow = len(nums)
    if nrow == 0:
        return 0
    ncol = len(nums[0])
    if ncol == 0:
        return 0
    res = [0]*ncol
    for i in range(nrow):
        for j in range(ncol):
            if i == 0 and j == 0:
                res[j] = nums[i][j]
            elif i == 0:
                res[j] = res[j-1] + nums[i][j]
            elif j == 0:
                res[j] = res[j] + nums[i][j]
            else:
                res[j] = max(res[j-1],res[j]) + nums[i][j] #这个地方改成min就可以求最小累积路径和了
    return res[-1]

if __name__ == "__main__":
    nums = [[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
    for row in nums:
        print(row)
    print(MaxPathSum(nums))
