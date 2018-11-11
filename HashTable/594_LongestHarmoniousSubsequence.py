# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode594: Longest Harmonious Subsequence问题

from collections import Counter

def findLHS(nums):
    #if len(nums) < 2:
    #    return 0
    dic = Counter(nums)
    sorted_keys = sorted(dic.keys())
    res = [dic[sorted_keys[i]]+dic[sorted_keys[i+1]] for i in range(len(sorted_keys)-1) if (sorted_keys[i+1]-sorted_keys[i]==1)]
    if res:
        return max(res)
    return 0

#其实巧妙利用字典的哈希性，可以规避上述解法中的排序
def findLHS2(nums):
    dic = {}
    for item in nums:
        dic[item] = dic.get(item,0) + 1
    LHS = 0
    for item, cnt in dic.items():
        if item+1 in dic:
            LHS = max(LHS, cnt+dic[item+1])
    return LHS

if __name__ == "__main__":
    nums = [1,3,4]
    print(nums)
    print(findLHS(nums))
    print(findLHS2(nums))
