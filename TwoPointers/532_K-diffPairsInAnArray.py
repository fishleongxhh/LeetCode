# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode532: K-diff Pairs in an Array问题

#用到了排序和两个指针的方法， 排序会大幅降低运算速度
def findPairs(nums, k):
    nums.sort()
    n = len(nums)
    if n <= 1:
        return 0
    start, end, cnt = 0, 1, 0
    while end <= n-1:
        target_num = nums[start] + k
        while end <= n-1 and nums[end] < target_num:
            end += 1
        if end > n-1:
            return cnt
        if nums[end] == target_num:
            cnt += 1
        start += 1
        while start <= n-1 and nums[start] == nums[start-1]:
            start += 1
        end = start + 1
    return cnt

from collections import Counter

def findPairs2(nums, k):
    cnt = 0
    if k == 0:
        my_dic = Counter(nums)
        for value in my_dic.values():
            cnt = cnt+1 if value > 1 else cnt
    elif k > 0:
        my_set = set(nums)
        for item in my_set:
            if item+k in my_set:
                cnt += 1
    else:
        cnt = 0
    return cnt

if __name__ == "__main__":
    nums = [1,3,6,2,4,5,7,8,9,8,5,3,2]
    k = 4
    print(sorted(nums), k)
    print(findPairs(nums[:], k))
    print(findPairs2(nums, k))
