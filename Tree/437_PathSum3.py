# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode437: Path Sum3问题

from Tree import *

#暴力法，时间复杂度O(Nlog(N))
def pathSumCore(root, target, data, cnt):
    if root:
        data.append(root.val)
        curr_sum = 0
        for item in data[::-1]:
            curr_sum += item
            if curr_sum == target:
                cnt[0] += 1
        pathSumCore(root.left, target, data, cnt)
        pathSumCore(root.right, target, data, cnt)
        data.pop()

#利用哈希表，时间复杂度O(N)
def pathSumCore2(root, target, dic, currSum):
    if root:
        currSum += root.val
        cnt = dic.get(currSum-target, 0)
        dic[currSum]  = dic.get(currSum, 0) + 1
        cnt += (pathSumCore2(root.left, target, dic, currSum) + pathSumCore2(root.right, target, dic, currSum))
        dic[currSum] -= 1
        return cnt
    return 0

def pathSum(root, sum):
    #data, cnt = [], [0]
    #pathSumCore(root, sum, data, cnt)
    #return cnt[0]
    dic = {0:1}
    return pathSumCore2(root, sum, dic, 0)

if __name__ == "__main__":
    nums = [5,3,1,2,4,8,6,7,9]
    root = initTree(nums)
    target = 6
    print(pathSum(root, target))
