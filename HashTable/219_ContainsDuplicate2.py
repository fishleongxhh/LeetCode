# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode219: Contains Duplicate2问题

def containsNearbyDuplicate(nums, k):
    dic = {}
    for loc, item in enumerate(nums):
        if (item in dic) and (loc-dic[item] <= k):
            return True
        else:
            dic[item] = loc
    return False

if __name__ == "__main__":
    nums = [1,2,3,1,2,3]
    k = 3
    print(nums, k)
    print(containsNearbyDuplicate(nums, k))
