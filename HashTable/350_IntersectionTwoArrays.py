# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode349: Intersection of Two Arrays 2, 需要使用到HashMap

def intersection(nums1, nums2):
    #先将一个数组转换成集合，并用一个字典记录出现的次数，然后遍历另一个数组
    set1, dic1 = set(), {}
    for item in nums1:
        if item in set1:
            dic1[item] += 1
        else:
            set1.add(item)
            dic1[item] = 1
    res = []
    for item in nums2:
        if item in set1:
            res.append(item)
            dic1[item] -= 1
            if dic1[item] == 0:
                set1.remove(item)
    return res

if __name__ == "__main__":
    nums1 = [1,2,2,2,3,3,1,1]
    nums2 = [1,1,1,2,3,2,3]
    print(nums1)
    print(nums2)
    print(intersection(nums1,nums2))
