# -*- coding: utf-8 -*-
# Author: Xu Hanhui
# 此程序使用快排的技巧来求出一个数组当中第K小的元素
# 对称地，也可以求出第K大的元素(即为第N+1-K小的元素)

#此函数用于调换start,mid,end三处的元素位置，使得start处的元素为三者中位数
def median3(nums, start, end):
    mid = (start+end)//2
    if nums[mid] > nums[start]:
        nums[start], nums[mid] = nums[mid], nums[start]
    if nums[start] > nums[end]:
        nums[start], nums[end] = nums[end], nums[start]
    if nums[mid] > nums[start]:
        nums[start], nums[mid] = nums[mid], nums[start]

def QuickSelectKernel(nums, start, end, K):
    #保存上下界
    low, high = start, end
    #调换元素顺序，使得start处为三处元素中位数
    median3(nums, start, end)
    #选区枢纽元
    pivot = nums[start]
    #循环，重排元素
    while start < end:
        while start < end:
            if nums[end] >= pivot:
                end -= 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                break
        while start < end:
            if nums[start] <= pivot:
                start += 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                break
    nums[start] = pivot
    #判断是否能够选取到第K小元素，如果不行就继续递归
    if start == K-1:
        return nums[start]
    elif start < K-1:
        item = QuickSelectKernel(nums, start+1, high, K)
        return item
    else:
        item = QuickSelectKernel(nums, low, start-1, K)
        return item

def QuickSelect(nums, K):
    n = len(nums)
    if K <= 0:
        print("K Should be Positive!")
        return None
    if n < K:
        print("The Length of Array is Smaller Than K!")
        return None
    item = QuickSelectKernel(nums, 0, n-1, K)
    return item

if __name__ == "__main__":
    nums = [3,6,2,4,67,78,45,5,65]
    K = 7
    print(sorted(nums), K)
    for K in range(1, len(nums)+1):
        print(QuickSelect(nums[:], K))
