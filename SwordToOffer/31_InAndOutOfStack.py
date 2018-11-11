# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序用来求解LeetCode31: 栈的压入弹出序列

def CheckStackInAndOut(nums1, nums2):
    stack, n1, n2 = [], len(nums1), len(nums2)
    k1 = k2 = 0
    while k2 < len(nums2):
        if (not stack) or stack[-1] != nums2[k2]:
            if k1 >= n1:
                return False
            else:
                stack.append(nums1[k1])
                k1 += 1
        else:
            stack.pop()
            k2 += 1
    if k1 < n1:
        return False
    else:
        return True

if __name__ == "__main__":
    nums1 = []
    nums2 = []
    print(nums1)
    print(nums2)
    print(CheckStackInAndOut(nums1,nums2))
