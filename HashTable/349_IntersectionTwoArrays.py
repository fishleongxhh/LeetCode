# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode349: Intersection of Two Arrays, 需要使用到HashMap

def intersection(nums1, nums2):
    #先将一个数组转换成集合，然后遍历另一个数组
    a_map = set(nums1)
    res = set()
    for item in nums2:
        if item in a_map:
            res.add(item)
    return list(res)

if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(nums1)
    print(nums2)
    print(intersection(nums1,nums2))
