# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode169: Majority Element，需要用到分治法

def majorityElement(nums):
    n = len(nums)
    if n == 0:
        return None
    ThisItem, ThisCnt = nums[0], 1
    for item in nums[1:]:
        if ThisCnt == 0:
            ThisItem, ThisCnt = item, 1
        else:
            ThisCnt = (ThisCnt+1) if item == ThisItem else (ThisCnt-1)
    #最后查看ThisItem是否是真正满足条件的元素
    AllCnt = len([item for item in nums if item == ThisItem])
    if AllCnt*2 > n:
        return ThisItem
    return None
    #return ThisItem #也可以默认，如果没有满足条件的元素，就返回最后一个ThisItem，这样就不用对ThisItem进行检查了

if __name__ == "__main__":
    nums = [2,1,2,1,1]
    print(nums)
    print(majorityElement(nums))
