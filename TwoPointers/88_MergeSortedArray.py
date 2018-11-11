# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode88: Merge Sorted Array问题

#假设nums1的长度足够长，超过m+n
def merge(nums1, m, nums2, n):
    end1, end2, end = m-1, n-1, m+n-1
    while end1 >=0 and end2 >=0:
        if nums1[end1] > nums2[end2]:
            nums1[end] = nums1[end1]
            end1 -= 1
        else:
            nums1[end] = nums2[end2]
            end2 -= 1
        end -= 1
    while end1 >= 0:
        nums1[end] = nums1[end1]
        end, end1 = end-1, end1-1
    while end2 >= 0:
        nums1[end] = nums2[end2]
        end, end2 = end-1, end2-1

if __name__ == "__main__":
    nums2 = [1,2,2,2,3,3,3,4,4,5,5,6,6,7,7,8,8,9]
    n = len(nums2)
    nums1 = [1,2,3] + [0]*n
    m = 3
    print(nums1, m , nums2, n)
    merge(nums1, m, nums2, n)
    print(nums1)
