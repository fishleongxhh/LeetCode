# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode724. Find Pivot Index问题

def pivotIndex(nums):
    if not nums:
        return -1
    CumSum, InvCumSum = [0], [0] #分别记录数组nums从首至尾以及从尾至首的累积和
    n = len(nums)
    for i in range(n-1):
        CumSum.append(CumSum[-1]+nums[i])
        InvCumSum.insert(0, InvCumSum[0]+nums[n-1-i])
    pivot = -1
    for i in range(n):
        if CumSum[i] == InvCumSum[i]:
            pivot = i
            break
    return pivot

if __name__ == "__main__":
    nums = [4,1,4,5,4,1,4]
    print(nums)
    pivot = pivotIndex(nums)
    print(pivot)
    if pivot != -1:
        print(sum(nums[:pivot]+[0]), sum(nums[(pivot+1):]+[0]))
