# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode566. Reshape the Matrix问题

def matrixReshape(nums, r, c):
    nrow, ncol = len(nums), len(nums[0])
    if nrow*ncol != r*c:
        return nums
    OneRow = []
    for row in nums:
        OneRow += row
    nums = []
    for i in range(r):
        nums.append(OneRow[i*c:(i+1)*c])
    return nums

if __name__ == "__main__":
    nums = [[1,2,3],[3,4,5]]
    for row in nums:
        print(row)
    r, c = 6,1
    res = matrixReshape(nums, r, c)
    for row in res:
        print(row)
