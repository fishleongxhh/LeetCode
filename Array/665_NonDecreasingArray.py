# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解665. Non-decreasing Array问题

def checkPossibility(nums):
    n = len(nums)
    bad_cnt, bad_loc = 0, 0
    for loc in range(n-1):
        if nums[loc] > nums[loc+1]:
            bad_cnt += 1
            if loc == 0:
                bad_loc = 0
            elif loc == n-2:
                bad_loc = n-1
            elif nums[loc-1] <= nums[loc+1]:
                bad_loc = loc
            else:
                bad_loc = loc+1
    flag = True
    if bad_cnt > 1:
        flag = False
    elif bad_cnt == 0:
        flag = True
    else:
        if bad_loc == 0 or bad_loc == n-1:
            flag = True
        elif nums[bad_loc+1] >= nums[bad_loc-1]:
            flag = True
        else:
            flag = False
    return flag

#上述解法讨论了很多特殊情况，下面是leetcode上的一个高效解
#思路与上类似，但是巧妙地避开了很多讨论
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = None
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if p is not None:
                    return False #一旦下降点超过1一次，立刻返回False
                p=i
        #至此，只用考虑没有下降点或者只有一个下降点的情况
        return (p is None or p==0 or p==len(nums)-2 or nums[p-1]<=nums[p+1] or nums[p]<=nums[p+2])

if __name__ == "__main__":
    nums = []
    print(nums)
    print(checkPossibility(nums))
