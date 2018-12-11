# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode4. Median of Two Sorted Arrays问题

#nums1和nums2非空
def findMedianSortedArrays(nums1, nums2):
    n1, n2 = len(nums1), len(nums2)
    n = n1+n2
    if n%2: #如果n为奇数
        res = findKth(nums1, nums2, n//2+1) #查找第n//2+1大的元素
    else:
        res = (findKth(nums1, nums2, n//2) + findKth(nums1, nums2, n//2+1))/2 #查找第n//2和第n//2+1大的元素，取平均
    return res

def findKth(nums1, nums2, k): #查找两个排序数组nums1和nums2中第k大的元素
    if not nums1:
        return nums2[k-1]
    if not nums2:
        return nums1[k-1]
    mid1, mid2 = len(nums1)//2, len(nums2)//2
    pivot1, pivot2 = nums1[mid1], nums2[mid2]
    #下面的一些关键阈值需要谨慎选取
    #如果是删除数组的左半部分，要保证删掉的部分长度小于k
    #如果是删除数组的右半部分，要保证剩下的部分长度大于等于k
    if mid1+mid2 < k-1:
        if pivot1 > pivot2: #此时第k大的元素必定不在nums2的左半部分
            return findKth(nums1, nums2[mid2+1:], k-mid2-1)
        else: #此时必定不在nums1的左半部分
            return findKth(nums1[mid1+1:], nums2, k-mid1-1)
    else:
        if pivot1 > pivot2: #此时必定不在nums1的右半部分
            return findKth(nums1[:mid1], nums2, k)
        else: #此时必定不在nums2的右半部分
            return findKth(nums1, nums2[:mid2], k)

if __name__ == "__main__":
    nums1 = [1,3,5,7,9,10,11]
    nums2 = [0,2,4,6,8,12,13,14,15,16,17]
    nums = sorted(nums1+nums2)
    print(nums1)
    print(nums2)
    print(nums)
    n = len(nums1)+len(nums2)
    if n%2:
        print(nums[n//2])
    else:
        print((nums[n//2-1]+nums[n//2])/2)
    print(findMedianSortedArrays(nums1, nums2))
